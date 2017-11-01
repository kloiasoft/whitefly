from mock import patch
from unittest import TestCase
from whitefly.models.workspace import Workspace


def always_true(instance):
    return True


def always_false(instance):
    return False


class TestWorkspace(TestCase):
    @patch('os.path.isdir')
    def test_workspace_data_dir_exists_should_return_true_when_data_dir_exists(self, path_isdir_mock):
        path_isdir_mock.side_effect = always_true

        workspace = Workspace("db", "oracle")
        ret = workspace.workspace_data_dir_exists()
        self.assertEqual(True, ret)

    @patch('os.path.isdir')
    def test_workspace_data_dir_exists_should_return_false_when_data_dir_not_exists(self, path_isdir_mock):
        path_isdir_mock.side_effect = always_false

        workspace = Workspace("db", "oracle")
        ret = workspace.workspace_data_dir_exists()
        self.assertEqual(False, ret)

    @patch('os.path.exists')
    def test_workspace_config_exists_should_return_true_when_config_exists(self, path_exists_mock):
        path_exists_mock.side_effect = always_true

        workspace = Workspace("db", "oracle")
        ret = workspace.workspace_config_exists()
        self.assertEqual(True, ret)

    @patch('os.path.exists')
    def test_workspace_config_exists_should_return_false_when_config_not_exists(self, path_exists_mock):
        path_exists_mock.side_effect = always_false

        workspace = Workspace("db", "oracle")
        ret = workspace.workspace_config_exists()
        self.assertEqual(False, ret)

    @patch('os.path.exists')
    @patch('os.path.isdir')
    def test_validate_should_return_true_when_data_dir_and_config_exists(self, path_exists_mock, path_isdir_mock):
        path_exists_mock.side_effect = always_true
        path_isdir_mock.side_effect = always_true

        workspace = Workspace("db", "oracle")
        ret = workspace.validate()
        self.assertEqual(True, ret)

    @patch('os.path.exists')
    @patch('os.path.isdir')
    def test_validate_should_return_false_when_data_dir_and_config_not_exists(self, path_exists_mock, path_isdir_mock):
        path_exists_mock.side_effect = always_false
        path_isdir_mock.side_effect = always_false

        workspace = Workspace("db", "oracle")
        ret = workspace.validate()
        self.assertEqual(False, ret)

