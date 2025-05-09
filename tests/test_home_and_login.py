import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.home_page import HomePage
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright

def test_home_and_login():
    print("✅ Test started...")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Go to homepage
        home = HomePage(page)
        home.go_to()
        page.wait_for_timeout(3000)  # Wait 3 seconds to see homepage
        assert home.is_homepage_loaded(), "❌ Homepage did not load"
        print("✅ Homepage loaded")

        # Auto-login
        login = LoginPage(page)
        login.login("farzanayeasmin2992@gmail.com", "123456789123")
        page.wait_for_timeout(5000)  # Wait 5 seconds after login
        print("✅ Logged in successfully")

        # Navigate to Jobs page
        page.click("text=Jobs")
        page.wait_for_timeout(3000)  # Wait 3 seconds to see Jobs page
        print("✅ Jobs page opened")

        browser.close()
        print("✅ Test completed successfully")

if __name__ == "__main__":
    test_home_and_login()
