class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = "#email"
        self.password_input = "#password"
        self.login_button = "button[type='submit']"

    def login(self, email, password):
        self.page.click("text=Login")  # Click Login button if not on login page
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
