import pytest
import yaml

from python1.calc import Calc

def steps():
    with open("../datas/steps.yaml") as f:
        return yaml.safe_load(f)

class Test_Calc:
    def setup(self):
        self.calc=Calc()
    # def test_add(self):
    #     result = self.calc.add(1,2)
    #     print(result)
    #     assert 3 == result
    @pytest.mark.parametrize('data1,data2,expect',
                             yaml.safe_load(open('../datas/b.yaml')))
    def test_add_1(self,data1,data2,expect):

        steps1 = steps()

        for step in steps1:
            print(f"step ==== >{step}")
            if 'add' == step:
                result = self.calc.add(data1,data2)
            elif 'add1' == step:
                result = self.calc.add1(data1,data2)
            print(result)
            assert  expect == result

        # result = self.calc.add(data1,data2)
        # print(result)
        # assert expect == result