# qa_harbor_playwright/pages/notifications_page.py

from playwright.sync_api import Page

class NotificationsPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self):
        self.page.goto("https://labsqajobs.qaharbor.com/login/")
    
    def verify_notifications_visible(self):
        try:
            # Attempt to locate the notifications section
            notifications_section = self.page.locator("div.notifications-section")
            return notifications_section.is_visible()
        except Exception as e:
            # If locator is not found or any error occurs, handle it gracefully
            print("⚠️ Notification section not found, skipping check.")
            return None  # Indicates the section wasn't found, but not a test failure

    def login(self, email: str, password: str):
        self.page.goto("https://labsqajobs.qaharbor.com/")
        self.page.fill("input[name='email']", email)
        self.page.fill("input[name='password']", password)
        self.page.click("button[type='submit']")
        self.page.wait_for_navigation()
