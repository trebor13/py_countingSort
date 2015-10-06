__author__ = 'Robert'

n = int(input())
ss = [''] * 100

h = n//2

for i in range(n):
    a,b = input().split()
    a = int(a)
    if i < h:
        ss[a] += '- '
    else:
        ss[a] += b + ' '


for i in range(100):
    print(ss[i], end = '')
