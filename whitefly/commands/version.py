import command
import whitefly.utils.release as release


class VersionCommand(command.BaseCommand):
    def execute(self, args):
        print("whitefly version " + release.VERSION + " (" + release.CODENAME + ")")
