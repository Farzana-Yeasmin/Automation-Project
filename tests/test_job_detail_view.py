import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.job_detail_page import JobDetailPage
from playwright.sync_api import sync_playwright

def test_view_job_details():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        job_page = JobDetailPage(page)

        # Login
        job_page.login("farzanayeasmin2992@gmail.com", "123456789123")

        # Navigate to Jobs
        job_page.go_to_jobs()

        # Click on first job title
        job_title = job_page.click_first_job_title()

        # Verify job details page loaded
        job_page.verify_job_detail_loaded()

        print(f"✅ Test Passed: Job details loaded for '{job_title}'")
        browser.close()

if __name__ == "__main__":
    test_view_job_details()
