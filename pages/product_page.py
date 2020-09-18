from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_prod_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), \
               "Button for add to basket not found!"
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def should_be_correct_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_ALERT).text, \
               "Name in basket not correct!"

    def should_be_correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_FROM_ALERT).text, \
               "Price in basket not correct!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), \
               "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), \
               "Success message not disappeared, but should be"
