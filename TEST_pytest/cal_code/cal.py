#被测对象
#实现计算器

class Calulator:
    #实现加法
    def add(self,a,b):
        return a+b
    #实现减法
    def subt(self,a,b):
        return a-b
    #实现乘法
    def multi(self,a,b):
        return a*b
    #实现出发
    def div(self,a,b):
        try:
            quo=a/b
            print(quo)
        except:
            print("除数不能为零")
