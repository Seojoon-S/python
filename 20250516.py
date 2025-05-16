
for i in range(10) :
    print(i, end = " ")

for i in range(10,21) :
    print(i, end = " ")

for i in range(1,10,2) :
    print(i, end = " ")

List = ["a", "b", "c"]
for s in List :
    print(s)

num_list = [1,2,3,4,5]
sum = 0
for num in num_list :
    sum += num
print("avg : %d" % (sum//5))

n = input()
for i in range(5) :
    print(n, end = " ")
print()

n    = int(input())
if (n<50) :
    for i in range(n,51) :
        print(i, end = " ")
elif (n>50) :
    for i in range(n, 49, -1) :
        print(i, end = " ")
else :
    print(50)

sum = 0
for i in range(5) :
    n = int(input())
    sum = sum + n
print("총합 : %d" % (sum))
print("평균 : %.2lf" % (sum/5))

sum = 0
cnt = 0
while True :
    n = int(input())
    if(n==-1) :
        break
    sum = sum +n
    cnt = cnt +1
print("합 : %d" % sum)
print("평균 : %.2lf"%(sum/cnt))

list = []
while True :
    n = int(input())
    if(n==-1) :
        break
    list.append(n)
print("합 : %d" % sum(list))
print("평균 : %.2lf"%(sum(list)/len(list)))

for i in range(3) :
    for j in range(1,6) :
        print(j, end = " ")
    print()

for j in range(5) :
    for j in range(5) :
        print("*", end = " ")
    print()

for i in range(2, 10) :
    print("< %d 단 >" % i)
    for j in range(1, 10) :
        print("%d * %d = %2d" % (i, j, i*j))
    print()

n = int(input("n : "))
for i in range(n) :
    for j in range(1, i+1):
        print("*", end = " ")
    print()

for i in range(1, n+1) :
    print("*"*i)

