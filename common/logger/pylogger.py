import logging
import logging.config


def init_py_logger():
    format = "@@ %(asctime)s %(levelname)-10s %(filename)-31s | %(message)s"
    format1 = "@@ %(asctime)s %(levelname)-10s %(lineno)-3s:%(filename)-31s| %(message)s" #  - %(funcName)30s()
    logging.basicConfig(format=format1, level=logging.DEBUG)


if __name__ == "__main__":
    #init_py_logger()
    logging.info("this is to test logger")
    logging.info("second msg in logger")
    logging.debug("debug msg from logger")
    logging.warning("a warning message from logger")
    logging.info("===================")