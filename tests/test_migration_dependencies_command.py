import sys
if sys.version_info[0] == 2:
    from StringIO import StringIO
else:
    from io import StringIO

from django.test import TestCase
from django.core.management import call_command, CommandError


class MigrationDependenciesCommandTestCase(TestCase):

    COMMAND_NAME = 'migration_dependencies'

    FOO_MIGRATIONS = [
        '0001_initial',
        '0002_auto_20170511_0514',
        '0003_auto_20170511_0514',
    ]

    BAR_MIGRATIONS = [
        '0001_initial',
        '0002_auto_20170511_0515',
    ]

    def setUp(self):
        self.out = StringIO()

    def test_call_without_apps_arguments_raise_command_error(self):
        """ Command call without applications lists should return usage info """
        with self.assertRaises(CommandError):
            call_command(self.COMMAND_NAME)

    def test_single_app_output_has_app_name(self):
        """ Should print application name """
        call_command(self.COMMAND_NAME, 'foo', stdout=self.out)
        self.assertIn('[foo]', self.out.getvalue())

    def test_print_all_migrations(self):
        """ Should print all migrations names """
        call_command(self.COMMAND_NAME, 'foo', stdout=self.out)
        output = self.out.getvalue()
        for migration in self.FOO_MIGRATIONS:
            self.assertIn('foo/{}'.format(migration), output)

    def test_print_depending_migrations(self):
        """ Should print depending migrations from another apps """
        call_command(self.COMMAND_NAME, 'foo', stdout=self.out)
        output = self.out.getvalue()
        self.assertIn('bar/0001_initial', output)

    def test_print_depends_on_migrations(self):
        call_command(self.COMMAND_NAME, 'foo', stdout=self.out)
        output = self.out.getvalue()
        self.assertIn('bar/0002_auto_20170511_0515', output)

    def test_multiple_apps_names(self):
        """ Should display multiple apps names """
        call_command(self.COMMAND_NAME, 'foo', 'bar', stdout=self.out)
        self.assertIn('[foo]', self.out.getvalue())
        self.assertIn('[bar]', self.out.getvalue())

    def test_display_all_provided_apps_migrations(self):
        """ Should display all migrations of all provided apps """
        call_command(self.COMMAND_NAME, 'foo', 'bar', stdout=self.out)
        output = self.out.getvalue()
        for migration in self.FOO_MIGRATIONS:
            self.assertIn('foo/{}'.format(migration), output)
        for migration in self.BAR_MIGRATIONS:
            self.assertIn('bar/{}'.format(migration), output)

    def test_not_existing_app(self):
        """ Should show error message if wrong application name was provided """
        call_command(self.COMMAND_NAME, 'wrong', stdout=self.out)
        self.assertIn('Migrations for `wrong` application were not found', self.out.getvalue())
