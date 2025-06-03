
def add(x,y) :
    s = x + y
    return s
result = add(10,20) + add(20,30)
print(result)


def f(n) :
    n = 20
    return n
n=10
f(n)
print(n)
n = f(n)
print(n)


def get_max(x,y) :
    if x > y :
        return x
    else :
        return y
x = int(input())
y = int(input())
n = get_max(x,y)
print(n)


def plus(x) :
    if x > 0 :
        return True
    else :
        return False
a = int(input())
print(plus(a))


def get_sum(n) :
    s = 0
    for i in range(1,n+1) :
        s += i
    return s
n = int(input())
print("1부터 %d까지의 합은 %d입니디." % (n, get_sum(n)))


def get_sum(a,b) :
    s = 0
    for i in range(a,b+1) :
        s += i
    return s
a = int(input())
b = int(input())
print("%d부터 %d까지의 합은 %d입니다." %(a,b,get_sum(a,b)))


def area(w,h) :
    return w * h
w = int(input())
h = int(input())
print(area(w,h))


def area(r) :
    return r ** 2 *3.14
r = float(input())
print(area(r))


def number(n) :
    if n % 2 == 0 :
        return "even"
    else :
        return "odd"
n = int(input())
print(number(n))


def square(a,b) :
    return a**b
a = int(input())
b = int(input())
print(square(a,b))


def get_sum(n) :
    s = 0
    for i in range (n) :
        s += int(input())
        return s
n = int(input("Enter integer n : "))
print("sum :", get_sum(n))
