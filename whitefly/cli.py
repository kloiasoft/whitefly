import re


class InvalidCommandException(Exception):
    pass


class CLI:
    def __init__(self):
        self.commands = [
            {"name": "help", "pattern": '\Ahelp', "module":"whitefly.commands.help", "klass": "HelpCommand"},
            {"name": "version", "pattern": '\Aversion', "module":"whitefly.commands.version", "klass": "VersionCommand"},
            {"name": "init.workspace", "pattern": '\Ainit\s+\w+\s+\w+', "module":"whitefly.commands.init", "klass": "WorkspaceCommand"},
            {"name": "init.help", "pattern": '\Ainit\s+help', "module":"whitefly.commands.init", "klass": "HelpCommand"},
            {"name": "env.list","pattern": '\Aenv\s+list',"module":"whitefly.commands.env", "klass": "ListCommand"},
            {"name": "env.add","pattern": '\Aenv\s+add\s+\w+\s+\w+', "module":"whitefly.commands.env", "klass": "AddCommand"},
            {"name": "env.help","pattern": '(\Aenv\s+help)|(\Aenv.*)', "module":"whitefly.commands.env", "klass": "HelpCommand"}
        ]

    def execute(self, args):
        command_str = ' '.join(args)
        for command in self.commands:
            p = re.compile(command["pattern"])
            if p.match(command_str):
                klass = self.load(command["module"], command["klass"])
                kommand = klass()
                kommand.execute(args)
                return
        klass = self.load('whitefly.commands.help', 'HelpCommand')
        kommand = klass()
        kommand.execute("")
        raise InvalidCommandException()

    def load(self, module, klass):
        module = __import__(module, fromlist=[klass])
        klass = getattr(module, klass)
        return klass
