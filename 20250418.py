'''
x=10
y=50
print("x : %d, y : %d" %(x,y))
print("x와 y는 같다?", x==y)
print("x와 y는 다르다?", x!=y)
print("x는 y보다 크다?", x>y)
print("x는 y보다 작다?", x<y)
print("x는 y보다 크거나 같다?", x>=y)
print("x는 y보다 작거나 같다?", x<=y)

x=True
y=False
print("x : %s, y : %s" %(x,y))
print("x and y =", x and y)
print("x or y =", x or y)
print("not x =", not x)
print("not x =", not y)

score = int(input("score : "))
if(score >= 60 and score <=100) :
    print("Pass")
else :
    print("Fail")

score = int(input("score : "))
if score >= 90 :
    print("A")
print("Pass")
    print("congratulation!")

score = int(input("score : "))
if score >=90 : 
    print("A")
elif score >= 60 :
    print("B")
else :
    print("C")

score = int(input("score : "))
if score >= 90 :
    print("A")
else :
    if score >=60 and score <= 89 :
        print("B")

x=10
print(x >= 0 and x <= 10)
print(x < 0 or x > 10)
print(not x)

a=int(input())
b=int(input())
c=int(input())
print(a>=140 and b>=140 and c>=140)

a=int(input())
b=int(input())
c=int(input())
if(a>=140 and b>=140 and c>=140) :
    print("True")
else :
    print("False")

a=int(input())
if(a==0) :
    print("0은 입력하지 마시오")
elif(a%2==1) :
    print("ODD")
else :
    print("EVEN")

y = int(input("year : "))
if(y%4==0 and y%100!=0) or (y%400==0) :
    print("leap year")
else :
    print("common year")

a = 1 in [1,2,3]
print(a)

a = 1 not in [1,2,3]
print(a)

case = ["Homework", "Eating", "Sleeping"]
if "Homework" in case :
    print("I have to do homework.")
else :
    print("It's break time.")
'''
import random
com = random.randint(1,2)
user = int(input("odd : 1, even : 2\n"))
print("COM(%d) : USER(%d)" %(com, user))
if com == user :
    print("Correct")
else :
    print("Incorrect")
