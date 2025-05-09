from playwright.sync_api import Page

class ProfilePage:
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

    def go_to_profile(self):
        self.page.wait_for_selector("text=Profile")
        self.page.click("text=Profile")
        self.page.wait_for_load_state("networkidle")
        assert "profile" in self.page.url
        print("✅ Navigated to Profile page.")

    def edit_profile_info(self, new_name, new_phone, new_address, new_bio, image_path):
        self.page.wait_for_selector("#name")
        self.page.fill("#name", new_name)
        self.page.fill("#phone", new_phone)
        self.page.fill("#address", new_address)
        self.page.fill("#bio", new_bio)

        # Upload profile picture
        self.page.set_input_files('input[type="file"]', image_path)
        print("✅ Profile picture uploaded.")

        self.page.click("button:has-text('Save')")
        print("✅ Submitted profile changes.")

    def verify_changes_saved(self, expected_name, expected_phone, expected_address, expected_bio):
        self.page.wait_for_selector("text=Changes saved")
        assert self.page.locator("text=Changes saved").is_visible()
        print("✅ Profile update confirmation message is visible.")

        # Confirm data was saved
        assert self.page.input_value("#name") == expected_name
        assert self.page.input_value("#phone") == expected_phone
        assert self.page.input_value("#address") == expected_address
        assert self.page.input_value("#bio") == expected_bio
        print("✅ All updated values are correctly displayed in the form.")
