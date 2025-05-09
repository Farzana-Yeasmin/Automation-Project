# qa_harbor_playwright/tests/test_invalid_resume_upload.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.resume_upload_page import ResumeUploadPage
from playwright.sync_api import sync_playwright

def test_invalid_resume_upload():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        resume_page = ResumeUploadPage(page)

        # Step 1: Login
        email = "farzanayeasmin2992@gmail.com"
        password = "123456789123"
        resume_page.login(email, password)
        print("✅ Logged in successfully")

        # Step 2: Navigate to upload section
        resume_page.go_to_resume_upload_section()
        print("✅ Opened resume upload section")

        # Step 3: Try uploading invalid file (.txt or .exe)
        invalid_file = os.path.abspath("invalid_resume.txt")  # Ensure this file exists
        resume_page.upload_resume(invalid_file)
        print("✅ Tried uploading invalid file")

        # Step 4: Check error message
        if resume_page.is_invalid_upload_message_visible():
            print("✅ Error shown: Invalid file format — test passed.")
        else:
            print("❌ No error shown for invalid file — test failed.")

        browser.close()

if __name__ == "__main__":
    test_invalid_resume_upload()
