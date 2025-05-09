import time
import string
import random
from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

    def generate_unique_name(self):
        return "user" + str(int(time.time()))

    def generate_unique_email(self):
        return f"user{int(time.time())}@gmail.com"

    def generate_random_password(self, length=8):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))

    def go_to_registration(self):
        self.page.goto("https://labsqajobs.qaharbor.com/login/")
        assert "login" in self.page.url
        self.page.click("text=Register")
        self.page.wait_for_url("https://labsqajobs.qaharbor.com/registration")
        assert "registration" in self.page.url
        self.page.click("text=Candidate")
        self.page.wait_for_url("https://labsqajobs.qaharbor.com/candidate-registration")
        assert "candidate-registration" in self.page.url
        print("✅ Navigated to candidate registration page")

    def register_candidate(self):
        name = self.generate_unique_name()
        email = self.generate_unique_email()
        password = self.generate_random_password()

        self.page.fill("#name", name)
        self.page.fill("#email", email)
        self.page.fill("#password", password)
        self.page.fill("#password_confirmation", password)
        self.page.click('button[type="submit"]')

        self.page.wait_for_timeout(6000)
        assert "account" in self.page.url
        print("✅ Registration successful.")
        print("➡️  Registered with:\n   Name:", name, "\n   Email:", email, "\n   Password:", password)
        return name, email, password

    def click_jobs_menu(self):
        self.page.wait_for_selector('text=Jobs')
        self.page.click('text=Jobs')
        self.page.wait_for_timeout(3000)
        print("✅ Navigated to Jobs page.")
