import logging
import subprocess
import os
import threading
import psutil

from common.constants import *
from common.logger.pylogger import init_py_logger
from common.utils.util import run_os_cmd

# FIXME::: add try catch blocks for failure scenarios


def __is_ssh_session_active_system(ssh_host_name: str):
    """
    checks if at least one ssh session is established for given hostname outside python program
    :param ssh_host_name: host name defined in ssh config file (~/.ssh/config)
    :return: true if at least one session is established else false
    """
    logging.info(f"checking if ssh session (in system level) is established for host '{ssh_host_name}'")
    process_list = list()
    for process in psutil.process_iter():
        if "ssh" in process.name().lower():
            process_list.append(process)
    for proc in process_list:
        cmdline = proc.cmdline()
        if ssh_host_name in cmdline:
            logging.info(f"ssh session for host '{ssh_host_name}' already exists")
            return True
    return False


def __is_ssh_session_active_python(ssh_host_name: str):
    """
    checks if at least one ssh session is established for given hostname in this active python console
    :param ssh_host_name: host name defined in ssh config file (~/.ssh/config)
    :return: true if at least one session is established else false
    """
    logging.info(f"checking if ssh session is established for host '{ssh_host_name}'")
    ssh_threads = [x for x in threading.enumerate() if x.name == CONTROLLER_SSH_SESSION_THREAD_NAME]
    if len(ssh_threads) == 0:
        logging.info("No active ssh sessions")
        return False
    logging.info(f"number of active ssh sessions = {len(ssh_threads)}")
    return True


def is_ssh_session_active(ssh_host_name: str):
    is_ssh_active = __is_ssh_session_active_python(ssh_host_name) | __is_ssh_session_active_system(ssh_host_name)
    return is_ssh_active

def __start_ssh(ssh_host_name: str):
    subprocess.call(f"ssh {ssh_host_name}", shell=True)
    pass


def start_shell_ssh_session(ssh_host_name: str):
    """
    Start a ssh session to given host defined in ssh config file (~/.ssh/config) if there is no existing session
    :param ssh_host_name: host name defined in ssh config file (~/.ssh/config)
    :return:
    """
    is_ssh_active = is_ssh_session_active(ssh_host_name)
    if is_ssh_active:
        logging.info("there is an existing active ssh session so not starting new one")
        return
    t = threading.Thread(target=__start_ssh, name=CONTROLLER_SSH_SESSION_THREAD_NAME, args=[ssh_host_name])
    t.daemon = True  # set daemon as true so that the thread is killed when python execution is stopped
    t.start()



if __name__ == "__main__":
    init_py_logger()
    logging.info("to test util functions.....")
    is_ssh_session_active1 = is_ssh_session_active("k-box")
    logging.info(f"is_ssh_session_active = {is_ssh_session_active1}")
    start_shell_ssh_session("k-box")
    is_ssh_session_active1 = is_ssh_session_active("k-box")
    logging.info(f"is_ssh_session_active === {is_ssh_session_active1}")

    start_shell_ssh_session("k-box")
    is_ssh_session_active1 = is_ssh_session_active("k-box")
    logging.info(f"is_ssh_session_active = {is_ssh_session_active1}")