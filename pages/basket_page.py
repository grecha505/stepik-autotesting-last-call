from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY)

    def should_be_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
