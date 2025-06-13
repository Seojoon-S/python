'''
def warning() :
    for i in range(3) :
        print("Fire!")
warning()

def two_times() :
    for i in range(1,10) :
        print("2 * %d = %d" % (i, 2 *1))
two_times()

from random import *
def random_number() :
    num = random() + 10
    return num
print(random_number())

def say(name) :
    print("Welcome,", name)
    return
say("SeoJoon")

def day(m,d) :
    print("Today is %s/%s." %(m,d))
m = int(input())
d = int(input())
day(m,d)

a = 0
def f() :
    global a
    global b
    print(a)
    a = 10
    b = 20
f()
print(a)
print(b)

def A() :
    print(1)
    r = B()
    print(r)
def B() :
    print(2)
    return 3
A()
print(4)

def f(n) :
    print(n)
    if n > 1 :
        f(n-1)
k = int(input())
f(k)

def f(n) :
    if n > 1 :
        f(n-1)
    print(n)
k = int(input())
f(k)

def factorial(n) :
    s = 1
    for i in range(1, n+1) :
        s = s * i
    return s
n = int(input())
print(factorial(n))

def factorial(n) :
    if n == 1 :
        return 1
    else :
        return n * factorial(n-1)
n = int(input())
print(factorial(n))

def judge(n) :
    if n > 0 :
        print("plus")
    elif n < 0 :
        print("minus")
    else :
        print("zero")
n = int(input())
judge(n)
'''
def season(n) :
    if 3<= n <= 5  :
        print("spring")
    elif 6<= n <= 8  :
        print("summer")
    elif 9<= n <= 11  :
        print("fall")
    elif n == 1 or n == 2 or n == 12 :
        print("winter")
    else :
        print("Error")
n = int(input())
season(n)
