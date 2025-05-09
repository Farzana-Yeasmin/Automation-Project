import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.registration_page import RegistrationPage
from playwright.sync_api import sync_playwright

def test_candidate_registration():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        registration_page = RegistrationPage(page)

        # Step 1: Go to registration page and select candidate
        registration_page.go_to_registration()

        # Step 2: Fill and submit registration form
        name, email, password = registration_page.register_candidate()

        # Step 3: Click on Jobs
        registration_page.click_jobs_menu()

        browser.close()

if __name__ == "__main__":
    test_candidate_registration()
