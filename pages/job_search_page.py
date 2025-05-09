from playwright.sync_api import Page

class JobSearchPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, email: str, password: str):
        """Login to the application."""
        self.page.goto("https://labsqajobs.qaharbor.com/login/")
        self.page.fill("#email", email)
        self.page.fill("#password", password)
        self.page.click('button[type="submit"]')
        self.page.wait_for_load_state("networkidle")
        assert "account" in self.page.url
        print("✅ Logged in successfully.")

    def open_jobs_page(self):
        """Navigate to the Jobs page."""
        self.page.wait_for_selector('text=Jobs')
        self.page.click('text=Jobs')
        self.page.wait_for_load_state("networkidle")

    def apply_location_filter(self, location: str):
        """Apply location filter to the job search."""
        self.page.wait_for_selector('text=Filter')
        self.page.click('text=Filter')

        self.page.wait_for_selector('select[name="location"]')
        self.page.select_option('select[name="location"]', label=location)
        self.page.click('button:has-text("Apply")')

    def verify_jobs_in_location(self, location: str):
        """Verify that all jobs listed are in the selected location."""
        self.page.wait_for_selector("text=" + location)

        job_cards = self.page.locator(".job-location")
        count = job_cards.count()
        for i in range(count):
            location_text = job_cards.nth(i).inner_text()
            assert location in location_text, f"❌ Found job outside {location}: {location_text}"

        print(f"✅ All listed jobs are in {location}.")
