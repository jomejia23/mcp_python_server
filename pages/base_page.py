from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        
    def navigate_to(self, url: str):
        self.page.goto(url)
        
    def get_element_text(self, selector: str) -> str:
        return self.page.text_content(selector)
    
    def is_element_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)
    
    def get_current_url(self) -> str:
        return self.page.url