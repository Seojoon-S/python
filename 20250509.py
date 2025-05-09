'''
i = 1
while i <=10 :
    print(i, end = " ")
    i += 1
'''
'''
sum = 0
i = 1
while i <= 100 :
    sum += i
    i += 1
print(sum)
'''
'''
n = int(input())
Sum = 0
i = 0
while i <= n :
    Sum = Sum +1
    i = i + 1
print(Sum)
'''
'''
while True :
    ans = input("Shall we close? (y/n) ")
    if ans == "y" :
        print("The end")
        break
'''
'''
n=int(input())
Sum = 0
i = 1
while True :
    Sum = Sum + i
    i = i + 1
    if i>n :
        break
print(Sum)
'''
'''
n= int(input())
i = 0
while True :
    i += 1
    if i % 2 == 0 :
        continue
    print(i, end = " ")
'''
'''
ans = " "
while ans != "Yes" :
    ans = input("Are you ready?")
    print("going out")
'''
'''
while True :
    ans = input("Are you ready?")
    if ans == "Yes" :
        print("going out")
        break
'''
'''
i = 0
while True :
    n = int(input("input :"))
    i = i + 1
    if i > 4 :
        break
    if n%5 == 0 :
        continue
    print("output : %d"% n)
'''
'''
Sum = 0
while True :
    n = int(input())
    if n ==0 :
        break
    Sum = Sum + n
print("output : %d"% Sum)
'''
'''
a = []
while True :
    n = int(input())
    if n == 0 :
        break
    a.append(n)
print("output : %d"% sum(a))
'''
'''
cnt = 0
n = int(input("정수 입력 : "))
while n > 0 :
    cnt += 1
    n //= 10
print("자릿수 : %d" % cnt)
'''
'''
ans = 0
n = int(input("정수 입력 : "))
while True :
    ans = ans + n % 10
    n = n // 10
    if n == 0 :
        break
    ans = ans * 10
print("뒤집은 수 : %d" % ans)
'''

import sys
import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("Tick Tock Timer")
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 36)
timer=0
while True :
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
    timer += 1
    screen.fill((255, 255, 255))
    cnt_txt = sysfont.render("Timer : %d"% timer, True, (0, 0, 0))
    screen.blit(cnt_txt, (140, 140))
    pygame.display.update()
    CLOCK.tick(1)
