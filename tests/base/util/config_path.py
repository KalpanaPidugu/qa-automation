
from os.path import join
from test import get_test_root_dir


def get_config_full_path(relative_path):
    base_dir = get_test_root_dir()
    file_full_path = join(base_dir, relative_path)
    return file_full_path
