"""
所有的被@装饰的装饰器函数不管是不是被显示的执行，只要使用了这种结构，他就会立马执行@所修饰的函数

"""

# 定义一个装饰器
def docorate(func):
    print("this is the decorate start")

    def innerFunc(out: str):
        print('this is the innerfunc,the out is:' + out)

    return innerFunc


@docorate
def testOuterFunc(out: int):
    print("this is the test outer func" + out)

#这个函数要成为一个带参数的装饰，如果被@装饰的函数，后面会被马上执行（在刚刚错误传参的时候其实也验证过）
#那么利用这一点，是的最外层带参数的这个函数返回一个原来的装饰器
def arguDecorate(lever:str):
    print("the lever is: "+lever)
    def innerDecoprate(func):
        def innerFunc(innerStr:str):
            print("this is the inner func,the argu is: "+innerStr)
        return innerFunc
    return innerDecoprate


"""
分析一下这个装饰器的执行流程
1.首先，由于arguDocorate被@所装饰，并且后面传入了参数，那么这个函数就被当作一个函数，立即执行
2.上面的最外层函数被执行完之后，返回了一个参数是函数指针的函数，这个函数其实是实际上的装饰器
3.就有点类似先执行函数，然后返回一个@xxx不带参数的装饰器？
"""
@arguDecorate("log")
def testArguDeco(argu:str):
    print("this is the testout func,the argu is: "+argu)


if __name__ == '__main__':
    #由于testOuterFunc被decorate装饰
    #首先，被装饰的函数会作为装饰器的一个指针（第一个？）传入到装饰器函数中
    #然后被装饰的函数名实际上就变成了由装饰器返回的函数了
    #testArguDeco("test")
    pass
