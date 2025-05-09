import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.job_application_page import JobApplicationPage
from playwright.sync_api import sync_playwright

def test_duplicate_apply():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        apply_page = JobApplicationPage(page)

        # Step 1: Login
        apply_page.login("farzanayeasmin2992@gmail.com", "123456789123")

        # Step 2: Go to Jobs
        apply_page.go_to_jobs()

        # Step 3: Open a job
        job_title = apply_page.open_first_job()

        # Step 4: Try to apply
        try:
            apply_page.apply_to_job()
        except:
            print("ℹ️ Possibly already applied before. Proceeding to check for duplicate message...")

        # Step 5: Try applying again to trigger duplicate message
        apply_page.try_duplicate_application()

        print(f"✅ Test Passed: Duplicate apply check completed for job: '{job_title}'")

        browser.close()

if __name__ == "__main__":
    test_duplicate_apply()
