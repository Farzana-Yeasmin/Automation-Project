import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.job_search_page import JobSearchPage
from playwright.sync_api import sync_playwright

def test_job_search_filter_by_location():
    """Test for job search with location filter."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Instantiate JobSearchPage class
        job_search_page = JobSearchPage(page)

        # Step 1: Login with credentials
        job_search_page.login("farzanayeasmin2992@gmail.com", "123456789123")

        # Step 2: Navigate to Jobs page
        job_search_page.open_jobs_page()

        # Step 3: Apply location filter (Dhaka)
        job_search_page.apply_location_filter("Dhaka")

        # Step 4: Verify that all jobs are located in Dhaka
        job_search_page.verify_jobs_in_location("Dhaka")

        # Step 5: Close the browser
        browser.close()

if __name__ == "__main__":
    test_job_search_filter_by_location()
