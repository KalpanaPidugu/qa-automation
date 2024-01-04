import logging
import unittest

#from tests.base.BaseTest  import BaseTest
#from common.config.controller_config import ControllerConfig
from common.controller import Controller
from common.logger.pylogger import init_py_logger
from common.utils.util import get_full_path
import json


class TestControllerApps(unittest.TestCase):
    controller = None
    def setUp(self):
        init_py_logger()
        logging.info("this is for local testing of controller class")
        # config = ControllerConfig.read_from_json(get_full_path("config_files/controler.json"))
        self.controller = Controller()
        logging.info("setting up for ValidateVocConfig test")

    def test(self):
        logging.info()



    def test_all_apps_online(self):
        process_status = self.controller.get_processes_status("VocoAutoprov")
        logging.info(f"status = {process_status}")
        self.assertEqual("online", process_status.lower())

        process_status = self.controller.get_processes_status("VocoTask")
        logging.info(f"status = {process_status}")
        self.assertEqual("online", process_status.lower())

        process_status = self.controller.get_processes_status("VocoBoxIo")
        logging.info(f"status = {process_status}")
        self.assertEqual("online", process_status.lower())

        process_status = self.controller.get_processes_status("VocoEndPoints")
        logging.info(f"status = {process_status}")
        self.assertEqual("online", process_status.lower())


    def test_validate_customer_json(self):

        # read json file from controller
        sftp_client = self.controller.ssh_client.open_sftp()
        customer_file = sftp_client.open("vocoapps/config/customer.json")
        text_bytes = customer_file.read() # output is of type bytes
        text_lines = text_bytes.decode("utf-8").split("\n") # converting to string and spliting lines
        json_no_comments = [l.split("//")[0] for l in text_lines] # removing comments
        removed_empty_lines = [l for l in json_no_comments if l.strip() != ""] # removing/filtering  empty lines
        joined_text_file = "\n".join(removed_empty_lines) # joining back to single string
        customer_json = json.loads(joined_text_file) # parsing to json

        # validating
        mandatory_enrolment = customer_json["mandatoryEnrolment"]
        self.assertFalse(mandatory_enrolment, "mandatoryEnrolment")
        print(customer_json)


