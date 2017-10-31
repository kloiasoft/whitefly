import os
import command
import json
import whitefly.utils.color as color
import whitefly.resources.readme as readme
import logging

logger = logging.getLogger(__name__)


class HelpCommand(command.BaseCommand):
    def execute(self, args):
        print("usage: whitefly init [db-type] [db-name]")


class WorkspaceCommand(command.BaseCommand):
    def __init__(self):
        self.WORKSPACE_DIR=".whitefly"
        self.validTypes = ["oracle","mongo","cassandra"]

    @staticmethod
    def generate_readme(type):
        return readme.CONTENT

    @staticmethod
    def generate_config(type):
        return json.dumps({"type": type, "environments": {}})

    @staticmethod
    def create_update_file(whitefly_dir, type):
        fo = open(os.path.join(whitefly_dir, "update.sql"), "w")
        fo.close()

    @staticmethod
    def create_rollback_file(whitefly_dir, type):
        fo = open(os.path.join(whitefly_dir, "rollback.sql"), "w")
        fo.close()

    def validate_type(self, type):
        if type not in self.validTypes:
            msg = color.RED + color.BOLD + type + color.END + " is not a valid type.\n"
            msg = msg + "\nValid types are:"
            for validType in self.validTypes:
                msg = msg + "\n\t* " + color.BOLD + validType + color.END
            raise Exception(msg)

    def create_whitefly_dir(self, whiteflyDir):
        os.mkdir(whiteflyDir)
        os.mkdir(os.path.join(whiteflyDir, self.WORKSPACE_DIR))

    def create_gitignore_file(self, whiteflyDir):
        fo = open(os.path.join(whiteflyDir, ".gitignore"), "w")
        fo.write(self.WORKSPACE_DIR)
        fo.close()

    def create_config_file(self, whiteflyDir, type):
        fo = open(os.path.join(whiteflyDir, ".whiteflyconfig"), "w")
        fo.write(self.generate_config(type))
        fo.close()

    def create_readme_file(self, whiteflyDir, type):
        fo = open(os.path.join(whiteflyDir, "README.md"), "w")
        fo.write(self.generate_readme(type))
        fo.close()

    def execute(self, args):
        try:
            type = args[1].lower()
            name = args[2].lower()
            self.validate_type(type)
            whiteflyDir = os.path.join(os.getcwd(), name)
            self.create_whitefly_dir(whiteflyDir)
            self.create_gitignore_file(whiteflyDir)
            self.create_config_file(whiteflyDir, type)
            self.create_readme_file(whiteflyDir, type)
            self.create_update_file(whiteflyDir, type)
            self.create_rollback_file(whiteflyDir, type)
            logger.info("Initialized empty whitefly workspace in " + whiteflyDir)
        except OSError, e:
            if e.errno == os.errno.EEXIST:
                raise Exception('Workspace is already created.')
            raise e
