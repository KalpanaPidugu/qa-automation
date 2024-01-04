import json
import logging

import paramiko
# import singleton as singleton
from paramiko import SSHClient
from fabric import Connection


#from common.config.controller_config import ControllerConfig
from common.logger.pylogger import init_py_logger
from common.paramiko_forward import forward_tunnel
from common.utils.ssh_utils import start_shell_ssh_session
from common.utils.util import get_full_path, read_env_var
import threading

#
# ENV_SETUP :: setup ssh config using private and public configs and also enable port forwarding in the config
# ENV_SETUP :: setup multipass chrome extension
# https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server


class Controller(object):
    ssh_client:SSHClient = None
    ssh_connection: Connection = None

    # This is to make the class singleton
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        #self.config = controller_config
        self.ssh_host_name = read_env_var("controller_ssh_config_host_name")
        self.__init_ssh_client()
        self.start_connections()

    def __init_ssh_client(self):
        self.ssh_connection = Connection(self.ssh_host_name)
        logging.getLogger("fabric").setLevel(level=logging.INFO)
        logging.getLogger("paramiko").setLevel(level=logging.INFO)
        logging.getLogger("invoke").setLevel(level=logging.INFO)
        self.ssh_client = self.ssh_connection.client

    def start_connections(self):
        start_shell_ssh_session(self.ssh_host_name)
        transport = self.ssh_client.get_transport()
        if transport is None or transport.authenticated == False:
            self.ssh_connection.create_session()


    def listdir(self, path) -> list:
        t = self.ssh_client.get_transport()
        return t.open_sftp_client().listdir(path)

    def get_processes_list(self):
        c = self.ssh_client
        stdin, stdout, stderr = c.exec_command("pm2 jlist")
        output = stdout.read()
        out_json_obj = json.loads(output.decode("utf-8"))
        return out_json_obj

    def execute_command(self, command):
        c = self.ssh_client
        stdin, stdout, stderr = c.exec_command(command)
        output = stdout.read().decode("utf-8")
        return output

    def get_processes_status(self, process_name: str):
        p_list = self.get_processes_list()
        proc_data = [p for p in p_list if p["name"].lower() == process_name.lower()]
        if len(proc_data) != 1:
            raise Exception(f"process {process_name} is not running correctly")
        proc_data = proc_data[0]
        status = proc_data["pm2_env"]["status"]
        uptime = proc_data["pm2_env"]["pm_uptime"]
        pid = proc_data["pid"]
        logging.info(f"app : {process_name}, status: {status}, uptime: {uptime}, pid: {pid}")
        return status





if __name__ == "__main__":
    init_py_logger()
    logging.info("this is for local testing of controller class")
    #config = ControllerConfig.read_from_json(get_full_path("config_files/controler.json"))
    controller =  Controller()
    status = controller.get_processes_status("VocoAutoprov")
    logging.info(f"status = {status}")
    status = controller.get_processes_status("VocoAutoprov")
    logging.info("================")
