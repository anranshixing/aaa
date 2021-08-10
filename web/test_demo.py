import pytest
import yaml


class TestDemo:

    @pytest.mark.parametrize("a,b",yaml.safe_load(open("./a.yaml")))
    def test_dmeo(self,a,b):
        print(a+b)