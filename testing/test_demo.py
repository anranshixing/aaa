import pytest
import yaml


class TestDemo:

    @pytest.mark.parametrize('a,b', yaml.safe_load(open("../datas/a.yaml")))
    # @pytest.mark.run(order=2)
    def test_dmeo(self, a, b):
        print(a + b)
    # @pytest.mark.zhangyao
    # @pytest.mark.run(order=1)
    def test_dmeo1(self, a=1, b=1):
        print(a + b)

if __name__=="__main__":
    pytest.main(['-vs',"test_demo.py::TestDemo::test_dmeo1"])
