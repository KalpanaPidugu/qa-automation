from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# class ChromeDriver:
#
#     def __init__(self):
#         self.create_driver()
#         pass
#
#     def create_driver(self):
#         self.driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
#
#     def open_page(self, url):
#         self.driver.get(url)
#
#     def close_driver(self):
#         self.driver.quit()
from common.utils.util import run_os_cmd


def open_web_page(host, port, page_name):
    # http://127.0.0.1:8100/SystemStatistics.html
    run_os_cmd(f"open http://{host}:{str(port)}/{page_name}.html")
    pass