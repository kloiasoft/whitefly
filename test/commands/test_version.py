from unittest import TestCase

from whitefly.commands.version import VersionCommand


class TestVersionCommand(TestCase):
    def test_message_shoult_return_help_message(self):
        expected = "whitefly version 0.0.2 (holmesii)"

        actual = VersionCommand.version()
        self.assertEqual(expected, actual)
