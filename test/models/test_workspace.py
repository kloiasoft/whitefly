import mock
from unittest import TestCase
from whitefly.models.workspace import Workspace


def always_true(instance):
    return True


def always_false(instance):
    return False


class TestWorkspace(TestCase):
    def test_workspace_data_dir_exists_should_return_true_when_data_dir_exists(self):
        path_isdir_patcher = mock.patch('os.path.isdir')
        path_isdir_mock = path_isdir_patcher.start()
        path_isdir_mock.side_effect = always_true

        workspace = Workspace("db", "oracle")
        ret = workspace.workspace_data_dir_exists()
        self.assertEqual(True, ret)

    def test_workspace_data_dir_exists_should_return_false_when_data_dir_not_exists(self):
        path_isdir_patcher = mock.patch('os.path.isdir')
        path_isdir_mock = path_isdir_patcher.start()
        path_isdir_mock.side_effect = always_false

        workspace = Workspace("db", "oracle")
        ret = workspace.workspace_data_dir_exists()
        self.assertEqual(False, ret)

    def test_workspace_config_exists_should_return_true_when_config_exists(self):
        path_exists_patcher = mock.patch('os.path.exists')
        path_exists_mock = path_exists_patcher.start()
        path_exists_mock.side_effect = always_true

        workspace = Workspace("db", "oracle")
        ret = workspace.workspace_config_exists()
        self.assertEqual(True, ret)

    def test_workspace_config_exists_should_return_false_when_config_not_exists(self):
        path_exists_patcher = mock.patch('os.path.exists')
        path_exists_mock = path_exists_patcher.start()
        path_exists_mock.side_effect = always_false

        workspace = Workspace("db", "oracle")
        ret = workspace.workspace_config_exists()
        self.assertEqual(False, ret)

    def test_validate_should_return_true_when_data_dir_and_config_exists(self):
        path_exists_patcher = mock.patch('os.path.exists')
        path_exists_mock = path_exists_patcher.start()
        path_exists_mock.side_effect = always_true

        path_isdir_patcher = mock.patch('os.path.isdir')
        path_isdir_mock = path_isdir_patcher.start()
        path_isdir_mock.side_effect = always_true

        workspace = Workspace("db", "oracle")
        ret = workspace.validate()
        self.assertEqual(True, ret)

    def test_validate_should_return_false_when_data_dir_and_config_not_exists(self):
        path_exists_patcher = mock.patch('os.path.exists')
        path_exists_mock = path_exists_patcher.start()
        path_exists_mock.side_effect = always_false

        path_isdir_patcher = mock.patch('os.path.isdir')
        path_isdir_mock = path_isdir_patcher.start()
        path_isdir_mock.side_effect = always_false

        workspace = Workspace("db", "oracle")
        ret = workspace.validate()
        self.assertEqual(False, ret)

