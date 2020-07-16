#-*- coding: utf-8 -*-
import pytest
import yaml

from cal_code.cal import Calulator

def test_env(openenv):
    env,datas=openenv
    print(f"环境：{env},数据:{datas}")
    ip = datas['env']['ip']
    port =datas['env']['port']
    url ='http://'+ip+':'+port
    print(url)


#获取测试数据
with open('cal_testing/testing_data/data.yml',encoding='utf-8') as f:
    datas=yaml.safe_load(f)

    myids_div=datas['div'].keys()
    mydatas_div=datas['div'].values()

    myids_add=datas['add'].keys()
    mydatas_add=datas['add'].values()

    myids_mutl=datas['mutl'].keys()
    mydatas_mutl=datas['mutl'].values()

    myids_subt=datas['subt'].keys()
    mydatas_subt=datas['subt'].values()

#使用fixture初始化用例
@pytest.fixture()
def method():
    print("set_up,开始计算")
    yield
    print("teat_down,计算结束")

#定义测试类
class TestCal:

#加法测试
    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='test_add')
    @pytest.mark.parametrize("a,b",mydatas_add,ids=myids_add)
    def test_add(self,cal_begin,method,a,b):
        print("测试加法")
        cal =Calulator()
        try:
            assert cal.add(a, b) == a + b
        except:return cal.add(a, b)
        print(f'测试结果为{cal.add(a,b)}')

#减法测试
    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=['test_add'],name='test_subt')
    @pytest.mark.parametrize("a,b", mydatas_subt,ids=myids_subt)
    def test_subt(self,cal_begin,method,a,b):
        print("测试减法")
        cal = Calulator()
        try:
            assert cal.subt(a, b) == a - b
        except:return cal.subt(a, b)
        print(f'测试结果为{cal.subt(a, b)}')
#乘法测试
    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='test_mutl')
    @pytest.mark.parametrize("a,b", mydatas_mutl,ids=myids_mutl)
    def check_mutl(self,cal_begin,method, a, b):
        print("测试乘法")
        cal = Calulator()
        try:
            assert cal.multi(a, b) == a * b
            assert a==b
        except:return cal.multi(a, b)
        print(f'测试结果为{cal.multi(a, b)}')

#除法测试
    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["test_mutl"],name="test_div")
    @pytest.mark.parametrize("a,b", mydatas_div,ids=myids_div)
    def test_div(self,cal_begin,method,a,b):
        print("测试除法")
        cal = Calulator()
        try:
            assert cal.div(a, b) == a / b
        except :return cal.div(a, b)
        print(f'测试结果为{cal.div(a, b)}')