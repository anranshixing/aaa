from test_qbjh.page.base_page import BasePage
from test_qbjh.page.experience import Experience
from test_qbjh.page.main import Main
from test_qbjh.page.shopping_cart import ShoppingCart


class Index(BasePage):


    def goto_experience(self):
        pass
        return Experience()

    def goto_shoppingcart(self):
        pass
        return ShoppingCart()

    def goto_main(self):
        pass
        return Main(self._driver)