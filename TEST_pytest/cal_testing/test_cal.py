#-*- coding: utf-8 -*-
import pytest
import yaml

from cal_code.cal import Calulator

@pytest.fixture()
def method():
    print("set_up,开始计算")
    yield
    print("teat_down,计算结束")
class TestCal:

    @pytest.mark.parametrize("a,b",yaml.safe_load(open("testing_data/data.yml",encoding='utf-8')),
                             ids=yaml.safe_load(open("testing_data/Casetitle_add.yml",encoding='utf-8')))
    def test_add(self,cal_begin,method,a,b):
        print("测试加法")
        cal =Calulator()
        try:
            assert cal.add(a, b) == a + b
        except:return cal.add(a, b)
        print(f'测试结果为{cal.add(a,b)}')

    @pytest.mark.parametrize("a,b", yaml.safe_load(open("testing_data/data_div.yml",encoding='utf-8')),
                             ids=yaml.safe_load(open("testing_data/Casetitle_subt.yml",encoding='utf-8')))
    def test_subt(self,cal_begin,method,a,b):
        print("测试减法")
        cal = Calulator()
        try:
            assert cal.subt(a, b) == a - b
        except:return cal.subt(a, b)
        print(f'测试结果为{cal.subt(a, b)}')

    @pytest.mark.parametrize("a,b", yaml.safe_load(open("testing_data/data.yml",encoding='utf-8')),
                        ids=yaml.safe_load(open("testing_data/Casetitle_mutl.yml",encoding='utf-8')))
    def test_mutl(self,cal_begin,method, a, b):
        print("测试乘法")
        cal = Calulator()
        try:
            assert cal.multi(a, b) == a * b
        except:return cal.multi(a, b)
        print(f'测试结果为{cal.multi(a, b)}')

    @pytest.mark.parametrize("a,b", yaml.safe_load(open("testing_data/data_div.yml",encoding='utf-8')),
                                    ids=yaml.safe_load(open("testing_data/Casetitle_div.yml",encoding='utf-8')))
    def test_div(self,cal_begin,method,a,b):
        print("测试除法")
        cal = Calulator()
        try:
            assert cal.div(a, b) == a / b
        except :return cal.div(a, b)
        print(f'测试结果为{cal.div(a, b)}')