from unittest import TestCase

from whitefly.commands.help import HelpCommand


class TestHelpCommand(TestCase):
    def test_message_shoult_return_help_message(self):
        expected = """usage: whitefly [--version] [--help] <command> [<args?]

These are common Whitefly commands used in various situations:

Start a working area:
init         Create an empty Whitefly workspace
env          Manage environments for the workspace"""

        actual = HelpCommand.message()
        self.assertEqual(expected, actual)
