from pages.login_page import LoginPage
from drivers.stealth_driver import create_driver

class LinkedInService:
    def __init__(self):
        self.driver = create_driver()

    def perform_login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.login(username, password)