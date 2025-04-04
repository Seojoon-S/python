
list1=[]
list2=[1, 2, 3]
list3=["a", "b", "c"]
list4=["hello", "world"]
list5=[1, 2, "a", "b", "python"]
list6=[1, 2, ["a", "b", "c"], 3]
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)

a = "Python"
b = " is fun"
print(a+b)
print(a*2)

a=[1,2,3]
b= [4,5,6]
print(a+b)
print(a*3)

a="Carpe Diem!"
print(a[6:11])
b="Carpe Diem!"
print(b[6:])

a=[10,20,30,40,50]
print(a[0])
b=[10,20,[30,40],50]
print(b[2])
print(b[2][0])
print(b[2][1])

a=[10,20,30,40,50]
print(a[1:4])

a=[1,2,"a","b",3,4,"c"]
print(a[5])                   #4
print(a[0:2])                #[1,2]
print(a[4:-1])               #[3,4]
print(a[0]+a[1])           #3 
print(a[2]+a[3]+a[6])   #abc

a=[10,20,30,40,50]
a[0]="a"
print(a)
a[1:3]="b"
print(a)

a="I Love You"
print(a.count("o"))
print(a.find("Y"), a.index("Y"))
print(".".join(a))
print(a.split())
print(a.replace("Love", "Like"))
print(a.upper(), a.lower())

a=" abcd "
b="efgh"
print("%s%s" %(a,b))
a=a.strip()
print("%s%s" %(a,b))

a="Hello World"
b="python"
c="oh!my!god"
print(a.count("l"))
print(b.find("p"))
print(c.split("!"))

a=[1,5,10,3]
a.append(20)
print(a)
a.sort()
print(a)
a=["b", "a", "n", "a", "n", "a"]
a.reverse()
print(a)
a.remove("a")
print(a)
p=a.pop()
print(p,a)
n=a.count("n")
print(n)

num=input("생년 월일 : ")
num=num.split("-")
print("출생 년도 : 20"+num[0]+"년")
print("태어난 달 : "+num[1]+"월")
print("태어난 일 : "+num[2]+"일")

a=[]
a.append(input("1 : "))
a.append(input("2 : "))
a.append(input("3 : "))
print(a)
