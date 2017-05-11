import sys
from io import StringIO

from django.test import TestCase
from django.core.management import call_command, CommandError


class MigrationDependenciesCommandTestCase(TestCase):

    COMMAND_NAME = 'migration_dependencies'

    AUTH_MIGRATIONS = [
        '0001_initial',
        '0002_alter_permission_name_max_length',
        '0003_alter_user_email_max_length',
        '0004_alter_user_username_opts',
        '0005_alter_user_last_login_null',
        '0006_require_contenttypes_0002',
        '0007_alter_validators_add_error_messages',
        '0008_alter_user_username_max_length',
    ]

    ADMIN_MIGRATIONS = [
        '0001_initial',
        '0002_logentry_remove_auto_add',
    ]

    def setUp(self):
        self.out = StringIO()
    
    def test_call_without_apps_arguments_raise_command_error(self):
        """ Command call without applications lists should return usage info """
        with self.assertRaises(CommandError):
            call_command(self.COMMAND_NAME)

    def test_single_app_output_has_app_name(self):
        """ Should print application name """
        call_command(self.COMMAND_NAME, 'auth', stdout=self.out)
        self.assertIn('[auth]', self.out.getvalue())

    def test_print_all_migrations(self):
        """ Should print all migrations names """
        call_command(self.COMMAND_NAME, 'auth', stdout=self.out)
        output = self.out.getvalue()
        for migration in self.AUTH_MIGRATIONS:
            self.assertIn('auth/{}'.format(migration), output)
    
    def test_print_depending_migrations(self):
        """ Should print depending migrations from another apps """
        call_command(self.COMMAND_NAME, 'auth', stdout=self.out)
        output = self.out.getvalue()
        self.assertIn('admin/0001_initial', output)

    def test_print_depends_on_migrations(self):
        call_command(self.COMMAND_NAME, 'auth', stdout=self.out)
        output = self.out.getvalue()
        self.assertIn('contenttypes/__first__', output)
        self.assertIn('contenttypes/0002_remove_content_type_name', output)

    def test_multiple_apps_names(self):
        """ Should display multiple apps names """
        call_command(self.COMMAND_NAME, 'auth', 'admin', stdout=self.out)
        self.assertIn('[auth]', self.out.getvalue())
        self.assertIn('[admin]', self.out.getvalue())

    def test_display_all_provided_apps_migrations(self):
        """ Should display all migrations of all provided apps """
        call_command(self.COMMAND_NAME, 'auth', 'admin', stdout=self.out)
        output = self.out.getvalue()
        for migration in self.AUTH_MIGRATIONS:
            self.assertIn('auth/{}'.format(migration), output)
        for migration in self.ADMIN_MIGRATIONS:
            self.assertIn('admin/{}'.format(migration), output)
