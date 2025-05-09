from playwright.sync_api import Page

class JobApplicationPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, email, password):
        self.page.goto("https://labsqajobs.qaharbor.com/login/")
        self.page.fill("#email", email)
        self.page.fill("#password", password)
        self.page.click('button[type="submit"]')
        self.page.wait_for_load_state("networkidle")
        assert "account" in self.page.url
        print("✅ Logged in successfully.")

    def go_to_jobs(self):
        self.page.wait_for_selector('text=Jobs')
        self.page.click('text=Jobs')
        self.page.wait_for_load_state("networkidle")
        print("✅ Navigated to Jobs page.")

    def open_first_job(self):
        self.page.wait_for_selector(".job-title")
        job_title_element = self.page.locator(".job-title").first
        job_title = job_title_element.inner_text()
        job_title_element.click()
        self.page.wait_for_selector("text=Job Description")
        print(f"✅ Opened job detail for: {job_title}")
        return job_title

    def apply_to_job(self):
        self.page.wait_for_selector("button:has-text('Apply')")
        self.page.click("button:has-text('Apply')")
        self.page.wait_for_selector("button:has-text('Confirm')")
        self.page.click("button:has-text('Confirm')")
        self.page.wait_for_selector("text=Application successful")
        assert self.page.locator("text=Application successful").is_visible()
        print("✅ Application successful message shown.")

    def try_duplicate_application(self):
        self.page.click("button:has-text('Apply')")
        self.page.wait_for_selector("button:has-text('Confirm')")
        self.page.click("button:has-text('Confirm')")
        self.page.wait_for_selector("text=Already applied")
        assert self.page.locator("text=Already applied").is_visible()
        print("✅ Duplicate application correctly blocked with message: 'Already applied'.")
