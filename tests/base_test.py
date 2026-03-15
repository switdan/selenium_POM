import unittest
from selenium import webdriver
from pages.home_page import HomePage
import subprocess
import time
import requests

class BaseTest(unittest.TestCase):
    """
    Base Test for each Test Case
    """

    @classmethod
    def setUpClass(cls):
        # Run docker-compose
        print("Starting docker-compose services...")
        subprocess.run(["docker", "compose", "up", "-d"], check=True)

        # Wait until HTTP will be available
        cls.wait_for_service("http://localhost:8080", timeout=30)

    @classmethod
    def tearDownClass(cls):
        # Turn off docker-compose after all tests
        print("Stopping docker-compose services...")
        subprocess.run(["docker", "compose", "down"], check=True)

    @classmethod
    def wait_for_service(cls, url, timeout=30, interval=1):
        """
        Wait until HTTP service not respond with code status 200
        """
        start_time = time.time()
        while True:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"Service at {url} is ready!")
                    return
            except requests.ConnectionError:
                pass  # service not started yet
            if time.time() - start_time > timeout:
                raise TimeoutError(f"Service {url} did not start in {timeout} seconds")
            time.sleep(interval)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()
        pass