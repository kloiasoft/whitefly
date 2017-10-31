import os

WORKSPACE_CONFIG = ".whiteflyconfig"
WORKSPACE_DATA_DIR = ".whitefly"


class Workspace(object):
    def __init__(self, name=None, type=None):
        self.name = name
        self.type = type
        self.dir = os.getcwd()
        self.data_dir = os.path.join(self.dir, WORKSPACE_DATA_DIR)
        self.config = os.path.join(self.dir, WORKSPACE_CONFIG)

    def workspace_data_dir_exists(self):
        return os.path.isdir(self.data_dir)

    def workspace_config_exists(self):
        return os.path.exists(self.config)

    def validate(self):
        if self.workspace_data_dir_exists() and self.workspace_config_exists():
             return True
        return False
