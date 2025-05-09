import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.job_search_page import JobSearchPage
from playwright.sync_api import sync_playwright

def test_job_search_by_title():
    """Test for job search functionality."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Instantiate JobSearchPage class
        job_search_page = JobSearchPage(page)

        # Step 1: Login with credentials
        job_search_page.login("farzanayeasmin2992@gmail.com", "123456789123")

        # Step 2: Perform job search for 'QA Engineer'
        job_search_page.search_job("QA Engineer")

        # Step 3: Close the browser
        browser.close()

if __name__ == "__main__":
    test_job_search_by_title()
