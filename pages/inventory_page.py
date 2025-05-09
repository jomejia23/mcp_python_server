from .base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.menu_button = '#react-burger-menu-btn'
        self.logout_link = '#logout_sidebar_link'
        self.inventory_container = '#inventory_container'
        
    def logout(self):
        self.page.click(self.menu_button)
        self.page.click(self.logout_link)
        
    def is_inventory_displayed(self) -> bool:
        return self.is_element_visible(self.inventory_container)