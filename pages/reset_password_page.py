# pages/reset_password_page.py

class ResetPasswordPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com/reset-password/"
        self.email_input = 'input[name="email"]'
        self.token_input = 'input[name="token"]'
        self.new_password_input = 'input[name="password"]'
        self.confirm_password_input = 'input[name="password_confirmation"]'
        self.submit_button = 'button[type="submit"]'

    def go_to(self):
        self.page.goto(self.url)

    def reset_password(self, email, token, new_password):
        self.page.fill(self.email_input, email)
        self.page.fill(self.token_input, token)
        self.page.fill(self.new_password_input, new_password)
        self.page.fill(self.confirm_password_input, new_password)
        self.page.click(self.submit_button)
