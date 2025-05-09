# qa_harbor_playwright/tests/test_resume_upload.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.resume_upload_page import ResumeUploadPage
from playwright.sync_api import sync_playwright

def test_resume_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        resume_page = ResumeUploadPage(page)

        # Step 1: Login automatically
        email = "farzanayeasmin2992@gmail.com"
        password = "123456789123"
        resume_page.login(email, password)
        print("✅ Logged in successfully")

        # Step 2: Go to Resume Upload section
        resume_page.go_to_resume_upload_section()
        print("✅ Navigated to Resume Upload section")

        # Step 3: Upload the resume
        pdf_file = os.path.abspath("farzana _212002009.pdf")  # Ensure this exists
        resume_page.upload_resume(pdf_file)
        print("✅ Resume file uploaded")

        # Step 4: Verify success
        if resume_page.is_upload_successful():
            print("✅ Resume uploaded successfully.")
        else:
            print("❌ Upload failed. Please check the file or selectors.")

        browser.close()

if __name__ == "__main__":
    test_resume_upload()
