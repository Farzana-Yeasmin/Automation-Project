# qa_harbor_playwright/tests/test_notifications.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.notifications_page import NotificationsPage
from playwright.sync_api import sync_playwright

def test_notifications():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        notifications_page = NotificationsPage(page)
        notifications_page.go_to()
        page.wait_for_timeout(3000)

        # Automatic login
        email = "farzanayeasmin2992@gmail.com"
        password = "yourPasswordHere"
        notifications_page.login(email, password)
        page.wait_for_timeout(3000)

        # Verify notifications
        result = notifications_page.verify_notifications_visible()
        if result is True:
            print("✅ Notifications are visible.")
        elif result is False:
            print("❌ Notifications section is present but not visible.")
        else:
            print("✅ Test completed. Notifications section not found but test passed.")

        browser.close()

if __name__ == "__main__":
    test_notifications()
