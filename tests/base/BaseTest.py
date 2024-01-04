import logging
import os
import unittest
from os.path import join
from pathlib import Path


"""
Base Test class to initialise test environment like logging 
"""


class BaseTest(unittest.TestCase):
    env = "unit_test"
    root_dir = ""
    test_root_dir = ""

    @classmethod
    def setUpClass(cls) -> None:
        pass

