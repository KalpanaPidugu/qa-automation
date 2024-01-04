import logging
from paramiko.client import SSHClient
from paramiko import SSHConfig

from common.controller import Controller
from dacite import from_dict, Config
from marshmallow_dataclass import dataclass

from common.utils.util import read_all_env_var


@dataclass
class BaseUnitData:
    mac_address: str
    ip_address: str = ""
    local_ui_port: int = 0
    is_primary: bool = False
    is_connected: bool = False


class BaseUnits(object):
    is_multi_cell_connected = False
    base_units_list: list[BaseUnitData] = list()
    controller: Controller = None

    # this is for singlton
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.controller = Controller()
        self.init_all_base_units()

    def init_all_base_units(self):
        # step1: read env vars from .env.test
        env_configs = read_all_env_var()
        # step2 : get all the env vars for base unit mac
        base_units_macs_keys = [m for m in env_configs.keys() if "mac" in m and "base_unit" in m]
        base_units_macs = [env_configs[k] for k in base_units_macs_keys]
        # step3 : get all the reachable ip address frpm controller
        cmd_out = self.controller.execute_command("ip n | grep lla").split("\n")
        # step4 : create baseUnit data class objects list
        self.base_units_list = [BaseUnitData(m) for m in base_units_macs]
        # step5 : read ssh config for port forwarding
        # ssh_config = "~/.ssh/config"
        # ssh_host = "k-box"
        # config = ssh_config()
        # config_file = open(config)
        # config.parse(config_file)
        # dev_config = config.lookup(ssh_host)
        #print("-------")

        # step6 : read VocoAutoprov logs from controller for primary baseunit identification

        # populate ip_address and is_connected fields
        for unit in self.base_units_list:
            ip_addr_line = [l for l in cmd_out if unit.mac_address in l.replace(":", "")]
            if len(ip_addr_line) == 1:
                l = ip_addr_line[0]
                ip_addr = l.split(" ")[0]
                unit.ip_address = ip_addr
                unit.is_connected = True
                # TODO :: add port forwarding
                # TODO :: add if its primary
        print("-------")
        pass

    def get_primary_base_unit(self):
        pass


if __name__ == "__main__":
    print("base units class")
    base_units = BaseUnits()
    print("---------")