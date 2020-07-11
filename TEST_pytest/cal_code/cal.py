#被测对象
#实现计算器

class Calulator:
    #实现加法
    def add(self,a,b):
        #return a+b
        try:
            sum = a + b
            return sum
        except Exception as erro:
            print(f"这里有一个错误{erro}")
    #实现减法
    def subt(self,a,b):
        try:
            diff = a - b
            return diff
        except Exception as erro:
            print(f"这里有一个错误{erro}")
    #实现乘法
    def multi(self,a,b):
        try:
            pro = a * b
            return pro
        except Exception as erro:
            print(f"这里有一个错误{erro}")
    #实现出发
    def div(self,a,b):
        try:
            quo=a/b
            return quo
        except Exception as erro:
            print(f"这里有一个错误{erro}")
