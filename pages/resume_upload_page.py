# qa_harbor_playwright/pages/resume_upload_page.py

from playwright.sync_api import Page

class ResumeUploadPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, email: str, password: str):
        self.page.goto("https://labsqajobs.qaharbor.com/login/")
        self.page.fill("input[name='email']", email)
        self.page.fill("input[name='password']", password)
        self.page.click("button[type='submit']")
        self.page.wait_for_load_state("networkidle")

    def go_to_resume_upload_section(self):
        try:
            self.page.click("text='Upload Resume'")
            self.page.wait_for_timeout(2000)
        except Exception:
            print("⚠️ Could not find the resume upload button.")

    def upload_resume(self, file_path: str):
        try:
            self.page.set_input_files("input[type='file']", file_path)
            self.page.wait_for_timeout(2000)
        except Exception as e:
            print("⚠️ Error uploading file:", e)

    def is_invalid_upload_message_visible(self):
        try:
            return self.page.locator("text='Invalid file format'").is_visible()
        except:
            return False
