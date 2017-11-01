from mock import patch
from unittest import TestCase
import whitefly.cli


class TestCLI(TestCase):

    @patch('whitefly.commands.help.HelpCommand')
    def test_execute_should_execute_help_command_when_invalid_command_given(self, MockCommand):
        try:
            cli = whitefly.cli.CLI()
            cli.execute(["asldkfj"])
        except whitefly.cli.InvalidCommandException as e:
            pass
        assert MockCommand.called

    def test_execute_should_throw_invalid_command_exception_when_invalid_command_given(self):
        cli = whitefly.cli.CLI()
        self.assertRaises(whitefly.cli.InvalidCommandException, cli.execute, "asldkfj")

    @patch('whitefly.commands.help.HelpCommand')
    def test_execute_should_execute_help_command_when_help_command_given(self, MockCommand):
        cli = whitefly.cli.CLI()
        cli.execute(["help"])
        assert MockCommand.called

    @patch('whitefly.commands.version.VersionCommand')
    def test_execute_should_execute_version_command_when_version_command_given(self, MockCommand):
        cli = whitefly.cli.CLI()
        cli.execute(["version"])
        assert MockCommand.called

    @patch('whitefly.commands.init.WorkspaceCommand')
    def test_execute_should_execute_workspace_command_when_init_oracle_db_command_given(self, MockCommand):
        cli = whitefly.cli.CLI()
        cli.execute(["init oracle db"])
        assert MockCommand.called

    @patch('whitefly.commands.init.HelpCommand')
    def test_execute_should_execute_help_command_when_init_help_command_given(self, MockCommand):
        cli = whitefly.cli.CLI()
        cli.execute(["init help"])
        assert MockCommand.called

    @patch('whitefly.commands.env.ListCommand')
    def test_execute_should_execute_list_command_when_env_list_command_given(self, MockCommand):
        cli = whitefly.cli.CLI()
        cli.execute(["env list"])
        assert MockCommand.called

    @patch('whitefly.commands.env.AddCommand')
    def test_execute_should_execute_add_command_when_env_add_command_given(self, MockCommand):
        cli = whitefly.cli.CLI()
        cli.execute(["env add dev localhost"])
        assert MockCommand.called

    @patch('whitefly.commands.env.HelpCommand')
    def test_execute_should_execute_helo_command_when_env_help_command_given(self, MockCommand):
        cli = whitefly.cli.CLI()
        cli.execute(["env help"])
        assert MockCommand.called
