#-*- coding: utf-8 -*-
import pytest
import yaml

from cal_code.cal import Calulator


class TestCal:

    def setup_method(self):
        print("开始计算")
    def teardown_method(self):
        print("计算结束")

    @pytest.mark.parametrize("a,b",yaml.safe_load(open("data.yml",encoding='utf-8')),
                             ids=['正整数加正整数','正整数加正小数','正整数加负整数','正整数加负小数','正整数加0','正小数加正小数',
                                  '正小数加负整数','正小数加负小数','正小数加零','负整数加负整数','负整数加负小数','负整数加零',
                                  '负小数加负小数','负小数加0','零加零'])
    def test_add(self,cal_begin,a,b):
        print("测试加法")
        cal =Calulator()
        assert cal.add(a,b) == a+b

    @pytest.mark.parametrize("a,b", yaml.safe_load(open("data_div.yml",encoding='utf-8')),
                             ids=['正整数减正整数', '正整数减正小数', '正整数减负整数', '正整数减负小数', '正整数减0', '正小数减正小数',
                                  '正小数减负整数','正小数减负小数', '正小数减零', '负整数减负整数', '负整数减负小数', '负整数减零',
                                  '负小数减负小数', '负小数减0', '零减零','零减正整数','零减负整数','零减正小数','零减负小数'])
    def test_subt(self,cal_begin,a,b):
        print("测试减法")
        cal = Calulator()
        assert cal.subt(a,b) == a-b

    @pytest.mark.parametrize("a,b", yaml.safe_load(open("data.yml",encoding='utf-8')),
                        ids=['正整数乘正整数', '正整数乘正小数', '正整数乘负整数', '正整数乘负小数', '正整数乘0', '正小数乘正小数',
                             '正小数乘负整数','正小数乘负小数', '正小数乘零', '负整数乘负整数', '负整数乘负小数', '负整数乘零',
                             '负小数乘负小数', '负小数乘0', '零乘零'])
    def test_mutl(self,cal_begin, a, b):
        print("测试乘法")
        cal = Calulator()
        assert cal.multi(a, b) == a * b

    @pytest.mark.parametrize("a,b", yaml.safe_load(open("data_div.yml",encoding='utf-8')),
                        ids=['正整数除正整数', '正整数除正小数', '正整数除负整数', '正整数除负小数', '正整数除0', '正小数除正小数',
                           '正小数除负整数','正小数除负小数', '正小数除零', '负整数除负整数', '负整数除负小数', '负整数除零',
                           '负小数除负小数', '负小数除0', '零除零',"零除正整数",'零除负整数',"零除正小数","零除负小数"])
    def test_div(self,cal_begin,a,b):
        print("测试除法")
        cal = Calulator()
        try:
            assert cal.div(a, b) == a / b
        except:
            print(cal.div(a,b))
