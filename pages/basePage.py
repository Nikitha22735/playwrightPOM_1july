from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click_element(self, selector: str):
        # Centralized logging + auto-waiting click
        print(f"Clicking on element: {selector}")
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def fill_text(self, selector: str, text: str):
        print(f"Typing '{text}' into {selector}")
        self.page.fill(selector, text)