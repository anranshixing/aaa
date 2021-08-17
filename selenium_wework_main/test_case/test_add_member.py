from selenium_wework_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_add_member(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        assert 'shixing' in add_member.get_member()


