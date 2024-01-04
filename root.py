import os
from pathlib import Path


def get_project_root_dir():
    return str(Path(__file__).parent)


def get_config_dir_path():
    root_dir = str(Path(__file__).parent)
    return os.path.join(root_dir, "config_files")


if __name__ == "__main__":
    print("====")
    print(f"get_project_root_dir = {get_project_root_dir()}")
    print(f"get_config_dir_path = {get_config_dir_path()}")