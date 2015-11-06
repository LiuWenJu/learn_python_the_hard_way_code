#coding=utf-8

class Parent(object):#创建一个父类

    def override(self):#定义override函数
        print "PARENT override()"#打印

    def implicit(self):#定义implicit函数
        print "PARENT implicit()"#打印

    def altered(self):#定义altered函数
        print "PARENT altered()"#打印

class Child(Parent):#创建一个Child类继承Parent()

    def override(self):#定义override函数
        print "CHILD override()"#打印

    def altered(self):#定义altered函数
        print "CHILD, BEFORE PARENT altered()"#打印
        super(Child, self).altered()#调用super,传入Child和self参数,不管结果如何调用altered()函数
        print "CHILD, AFTER PARENT altered()"#打印


dad = Parent()#设置dad为Parent的一个实例
son = Child()#设置son为Child的一个实例


dad.implicit()#调用dad的implicit函数
son.implicit()#调用son的implicit函数

dad.override()#调用dad的override函数
son.override()#调用son的override函数

dad.altered()#调用dad的altered函数
son.altered()#调用son的altered函数


