from selenium_weixinwork_login.index import Index


class TestRegister:
    def setup(self):
        self.index = Index()
    def test_register(self):
        self.index.goto_login().goto_register().register()

