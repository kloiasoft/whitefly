import command
import json
from whitefly.models.workspace import Workspace
from whitefly.utils.linebuilder import LineBuilder


def validate_workspace():
    workspace = Workspace()
    if not workspace.validate():
        raise Exception("Not a whitefly workspace")


class ListCommand(command.BaseCommand):
    NAME = "NAME"
    CONNECTION_STRING = "CONNECTION STRING"
    USERNAME = "USERNAME"
    PASSWORD = "PASSWORD"
    TAB = "/t"

    def execute(self, args):
        validate_workspace()
        line_builder = LineBuilder()
        fo = open(".whiteflyconfig", "r")
        conf_content = fo.read()
        conf = json.loads(conf_content)
        (line_builder.append_short(self.NAME)
            .append_long(self.CONNECTION_STRING)
            .append_short(self.USERNAME)
            .append_short(self.PASSWORD)
            .println())
        for env in conf["environments"]:
            (line_builder.append_short(env.get("name"))
                .append_long(env.get("connection-string"))
                .append_short(env.get("username"))
                .append_short(env.get("password"))
                .println())

            print(self.NAME + self.TAB + self.CONNECTION_STRING + self.TAB + self.USERNAME + self.TAB + self.PASSWORD)


class HelpCommand(command.BaseCommand):
    def execute(self, args):
        print("""usage: whitefly env list
         whitefly env add <name> <connection-string>
         whitefly env update <name> <connection-string>
         whitefly env remove <name>""")


class AddCommand(command.BaseCommand):
    def execute(self, args):
        name = args[0]
        type = args[1]
        validate_workspace()

