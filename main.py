from flask import Flask
#装饰器相当于在函数外面包一层函数，扩展原来函数的功能，只只不过通过python提供了一种语法糖，来简单的调用这个函数

#装饰器
def Debug(func):
    def warp(argu):
        print("this is warp:"+func.__name__);
        return warp #这里的warp仅仅只是一个对象