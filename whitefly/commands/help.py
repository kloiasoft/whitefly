import command


class HelpCommand(command.BaseCommand):
    def execute(self, args):
        print("usage: whitefly [--version] [--help] <command> [<args?]")
        print("")
        print("These are common Whitefly commands used in various situations:")
        print("")
        print("Start a working area:")
        print("init         Create an empty Whitefly workspace")
        print("env          Manage environments for the workspace")
