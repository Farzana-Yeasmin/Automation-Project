class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://labsqajobs.qaharbor.com"

    def go_to(self):
        self.page.goto(self.url)

    def is_homepage_loaded(self):
        return "qaharbor" in self.page.url
