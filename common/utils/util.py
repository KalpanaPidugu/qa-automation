import json
import logging
import os
from os.path import expandvars
from re import findall
import subprocess
from dotenv import dotenv_values

from common.logger.pylogger import init_py_logger
from root import get_project_root_dir


def get_full_path(relative_path: str):
    return os.path.join(get_project_root_dir(), relative_path)


def read_json_file(file_path: str) -> dict:
    json_config = {}
    with open(file_path, "r") as json_file:
        json_config = json.load(json_file)
    return json_config

def run_os_cmd(cmd: list) -> str:
    """
    rus command on os terminal and returns unprocessed output of the command
    :param cmd: command to run (Example : ["ls", "-la"]
    :return: output of the command, if command is not executed properly, None is returned
    """
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        output = result.stdout #.decode('utf-8')
        return output
    except Exception as e:
        logging.ERROR(str(e))
        logging.ERROR(f"failed to execute command {cmd}")
        return None

def read_env_var(env_var_name: str) -> str:
    env_file_path = os.path.join(get_project_root_dir(), ".env.test")
    config = dotenv_values(env_file_path)
    return config.get(env_var_name)

def read_all_env_var() -> dict:
    env_file_path = os.path.join(get_project_root_dir(), ".env.test")
    config = dotenv_values(env_file_path)
    return config


if __name__ == "__main__":
    init_py_logger()
    print(read_env_var("test"))
    print(read_env_var("controller_ssh_config_host_name"))
    logging.info("to test util functions.....")
    resp = run_os_cmd(["w"])
    respl = str(resp).split("\n")
    logging.info(f"response = {resp}")