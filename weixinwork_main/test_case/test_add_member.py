from weixinwork_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()

    def test_add_member(self):
        for i in range(10):
            add_member = self.main.goto_add_member()
            add_member.add_member()
            assert 'qwer' in add_member.get_member()
