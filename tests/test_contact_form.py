# qa_harbor_playwright/tests/test_contact_form.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.contact_page import ContactPage
from playwright.sync_api import sync_playwright

def test_contact_form_submission_auto():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        contact_page = ContactPage(page)

        # Step 1 & 2: Auto-login and auto-navigate to Contact
        email = "farzanayeasmin2992@gmail.com"
        password = "123456789123"
        contact_page.login_and_go_to_contact(email, password)
        print("✅ Logged in and reached Contact page")

        # Step 3: Submit form
        contact_page.submit_contact_form(
            name="Farzana Yasmin",
            email="farzanayeasmin2992@gmail.com",
            message="This is a test contact message via automation."
        )
        print("✅ Submitted contact form")

        # Step 4: Verify
        if contact_page.is_success_message_visible():
            print("✅ Contact message sent successfully — Test Passed.")
        else:
            print("❌ No success message shown — Test Failed.")

        browser.close()

if __name__ == "__main__":
    test_contact_form_submission_auto()
