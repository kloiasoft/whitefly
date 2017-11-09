import command
import whitefly.utils.release as release


class VersionCommand(command.BaseCommand):
    @staticmethod
    def version():
        return "whitefly version " + release.VERSION + " (" + release.CODENAME + ")"

    def execute(self, args):
        print(VersionCommand.version())
