import numpy as np


def printArray(arr,changeLine = 2,splitChar = ",", indent = 0):
    """
        打印数组的函数
        arr: 输入数组
        changeLine(1):换行深度
        splitChar("."):分割字符
        indent(0):缩进大小
    """
    # 前置括号
    print("  "*indent + "[",end = "")
    if changeLine > 0:
        print()
        print("  "*indent ,end = "")
    #打印主体
    for obj in arr:
        if changeLine <= 0:
            print(obj,end = splitChar)
        elif type(obj) is not list:
            print(obj,end = splitChar)
            print()
        else:
            #如果还是数切未达深度 递归调用
            printArray(obj, changeLine = changeLine - 1,splitChar = splitChar,indent = indent + 1)
    # 后置括号
    if changeLine > 0:
        print()
        print("  "*indent,end = "")
    print("]")

def printArray_NP(arr):
    """
        打印数组函数,调用Numpy
    """
    print(np.array(arr))