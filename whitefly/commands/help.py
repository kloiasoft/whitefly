import command


class HelpCommand(command.BaseCommand):

    @staticmethod
    def message():
        return """usage: whitefly [--version] [--help] <command> [<args?]

These are common Whitefly commands used in various situations:

Start a working area:
init         Create an empty Whitefly workspace
env          Manage environments for the workspace"""

    def execute(self, args):
        print(HelpCommand.message())
