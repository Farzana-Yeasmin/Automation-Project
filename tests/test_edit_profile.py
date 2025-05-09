import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.profile_page import ProfilePage
from playwright.sync_api import sync_playwright

def test_edit_profile_with_image():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        profile = ProfilePage(page)

        # Step 1: Login
        profile.login("farzanayeasmin2992@gmail.com", "123456789123")

        # Step 2: Go to Profile
        profile.go_to_profile()

        # Step 3: Prepare data
        timestamp = str(int(time.time()))
        new_name = f"Farzana {timestamp}"
        new_phone = f"0171{timestamp[-6:]}"
        new_address = "123 QA Avenue, Dhaka"
        new_bio = f"Passionate QA tester since {timestamp}"
        image_path = os.path.abspath("assets/profile.jpg")  # 🔁 Ensure this image exists in your project folder

        # Step 4: Edit profile including picture
        profile.edit_profile_info(new_name, new_phone, new_address, new_bio, image_path)

        # Step 5: Verify all updates
        profile.verify_changes_saved(new_name, new_phone, new_address, new_bio)

        print("✅ Test Passed: Profile updated with picture.")
        browser.close()

if __name__ == "__main__":
    test_edit_profile_with_image()
