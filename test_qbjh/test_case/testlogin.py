from test_qbjh.page.index import Index


class TestLogin:

    def setup(self):
        self.index = Index()

    def teardown(self):
        self._driver.quit()



    def test_login(self):
        self.index.goto_main().goto_login()