# tests/test_reset_password.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.reset_password_page import ResetPasswordPage
from playwright.sync_api import sync_playwright

def test_reset_password():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Open Reset Password Page
        reset_page = ResetPasswordPage(page)
        reset_page.go_to()
        page.wait_for_timeout(3000)
        print("✅ Opened reset password page")

        # 👉 Replace these with actual values from your email link
        email = "farzanayeasmin2992@gmail.com"
        token = "abc123"

        new_password = "123456789012"

        reset_page.reset_password(email, token, new_password)
        page.wait_for_timeout(4000)

        if "login" in page.url:
            print("✅ Password reset successful. Redirected to login page.")
        else:
            print("❌ Password reset may have failed. Check inputs or token.")

        browser.close()

if __name__ == "__main__":
    test_reset_password()
