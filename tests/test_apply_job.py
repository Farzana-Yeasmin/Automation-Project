import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.job_application_page import JobApplicationPage
from playwright.sync_api import sync_playwright

def test_apply_to_job():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        apply_page = JobApplicationPage(page)

        # Login as valid user
        apply_page.login("farzanayeasmin2992@gmail.com", "123456789123")

        # Navigate to jobs and open a job
        apply_page.go_to_jobs()
        job_title = apply_page.open_first_job()

        # Apply to the job
        apply_page.apply_to_job()

        print(f"✅ Test Passed: Successfully applied to job: '{job_title}'")
        browser.close()

if __name__ == "__main__":
    test_apply_to_job()
