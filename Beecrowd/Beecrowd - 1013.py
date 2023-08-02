'''
URI Online Judge | 1013
O Maior
'''

a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

maiorAB = (a+b + abs(a-b))/2

if maiorAB > c:
    print(f"{maiorAB:.0f} eh o maior")
else:
    print(f"{c:.0f} eh o maior")