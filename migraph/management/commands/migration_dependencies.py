from django.core.management.base import AppCommand
from django.db.migrations.loader import MigrationLoader


class Command(AppCommand):

    def print_label(self, text):
        self.stdout.write(self.style.MIGRATE_LABEL(text) + '\n')

    def print_warn(self, text):
        self.stdout.write(self.style.WARNING(text) + '\n')

    def print_title(self, text):
        self.stdout.write(self.style.MIGRATE_HEADING(text) + '\n')

    def print_notice(self, text):
        self.stdout.write(self.style.NOTICE(text) + '\n')

    def print_error(self, text):
        self.stdout.write(self.style.ERROR(text) + '\n')

    def print_success(self, text):
        try:
            styled_text = self.style.SUCCESS(text)
        except AttributeError:
            styled_text = self.style.MIGRATE_SUCCESS(text)
        self.stdout.write(styled_text + '\n')

    def handle(self, *apps, **options):
        self.loader = MigrationLoader(None)
        for app in apps:
            self.print_success("[{}]".format(app))
            self._print_app_migrations_graph(app)
            if app != apps[-1]:
                self.stdout.write('\n')

    def _print_app_migrations_graph(self, app):
        try:
            root_key = self.loader.graph.root_nodes(app)[0]
        except IndexError:
            self.print_error("Migrations for `{}` application were not found".format(app))
            return
        root_node = self.loader.graph.node_map[root_key]
        nodes_to_process = [root_node]
        processed = []
        while nodes_to_process:
            curr_node = nodes_to_process.pop(0)
            processed.append(curr_node)
            self._print_node(curr_node)
            depending_nodes = []
            for child in curr_node.children:
                if (child.key[0] == curr_node.key[0]) and (child not in nodes_to_process) and (child not in processed):
                    nodes_to_process.append(child)
                elif child.key[0] != curr_node.key[0]:
                    depending_nodes.append(child)
            self._print_depending_nodes(depending_nodes)
            self._print_depends_on(curr_node, self.loader.graph.nodes[curr_node.key])

    def _print_node(self, node):
        self.print_label("{}/{}".format(*node.key))

    def _print_depending_nodes(self, depending_nodes):
        if depending_nodes:
            self.print_title("\tDepending:")
            for depending in depending_nodes:
                self.print_warn("\t\t{}/{}".format(*depending.key))

    def _print_depends_on(self, node, migration):
        deps = [dep for dep in migration.dependencies if dep[0] != node.key[0]]
        if deps:
            self.print_title("\tDepends on:")
            for dep in deps:
                    self.print_notice("\t\t{}/{}".format(*dep))
