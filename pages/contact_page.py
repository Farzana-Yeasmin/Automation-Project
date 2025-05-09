# qa_harbor_playwright/pages/contact_page.py

from playwright.sync_api import Page

class ContactPage:
    def __init__(self, page: Page):
        self.page = page

    def login_and_go_to_contact(self, email: str, password: str):
        # Step 1: Go to login and authenticate
        self.page.goto("https://labsqajobs.qaharbor.com/login/")
        self.page.fill("input[name='email']", email)
        self.page.fill("input[name='password']", password)
        self.page.click("button[type='submit']")
        self.page.wait_for_load_state("networkidle")

        # Step 2: After login, navigate to Contact page (auto)
        try:
            self.page.click("text='Contact'")
            self.page.wait_for_timeout(2000)
        except Exception:
            print("⚠️ Could not find Contact link. Check if it's visible post-login.")

    def submit_contact_form(self, name: str, email: str, message: str):
        self.page.fill("input[name='name']", name)
        self.page.fill("input[name='email']", email)
        self.page.fill("textarea[name='message']", message)
        self.page.click("button[type='submit']")
        #self.page.wait_for_timeout(2000)

    def is_success_message_visible(self):
        return self.page.locator("text='Message sent successfully'").is_visible()
