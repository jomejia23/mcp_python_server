from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = '[data-test="username"]'
        self.password_input = '[data-test="password"]'
        self.login_button = '[data-test="login-button"]'
        self.error_message = '[data-test="error"]'
        
    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        
    def get_error_message(self) -> str:
        return self.get_element_text(self.error_message)
    
    def has_error_message(self) -> bool:
        return self.is_element_visible(self.error_message)