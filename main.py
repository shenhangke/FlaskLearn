from flask import Flask
#装饰器相当于在函数外面包一层函数，扩展原来函数的功能，只只不过通过python提供了一种语法糖，来简单的调用这个函数

"""
#装饰器
def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper

def say_hello():
    print("hello!")

say = debug(say_hello)  # 添加功能并保持原函数名不变

#say()   #其实这里调用的是wrapper函数，在wrapper函数return部分，调用了func，返回func函数的返回值

#所以所谓的装饰器，他所修饰的函数会返回一个函数？
#但是上面的代码并没有使用到装饰器，那么我们真实的使用一下装饰器呢

@debug
def say_hello_decorate():
    print("this is the func which has deccorate by @")

say_hello_decorate():"""
#所以实际上装饰器的作用就是加上了一个外层包装，让执行这个函数之前会执行一些其他已经定义好的代码
#而被装饰器修饰的函数传入的参数是一个函数指针，并且这个函数应该返回一个函数指针，这个函数可以是无预定义的

def debug_other(func):
    print("this is the direct call decorate func")
    def innerfunc():
        print("this is direct inner func")  #理论上，这里应该是要返回这个函数的，但是这里并没有返回这个函数？？？
        #或者说，函数执行到这里就报错？
        return func()
    return innerfunc()  #这里要注意的是，并没有真正的制定传进来的函数，看看是否可以执行

@debug_other
def say_hello_dir():
    print("this is the func which decorate by dir")  #这里这个函数也同时被执行了？？但是我在代码中并没有调用到这个函数啊

say_hello_dir()
#在这里报错了？为什么呢，难道得到的函数必须使用到下面的定义的函数？
#从语法上不应当做这种限制啊。。。





"""
def debug(func):
    def wrapper():
        print "[DEBUG]: enter {}()".format(func.__name__)
        return func()  #wrapper函数返回的是外层函数传进来的函数
    return wrapper  #外层函数的返回值返回的是内部定义的这个函数

def say_hello():
    print "hello!"

say_hello = debug(say_hello)  # 添加功能并保持原函数名不变

#如果调用debug(say_hello)函数的话，实际上返回值say_hello是wrapper函数
"""