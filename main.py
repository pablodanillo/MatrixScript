import re

n,m=map(int,input().split())
l=list()
for i in range(n):
    l.append(input())
l=list(zip(*l))
s=''
for i in l:
    s=s+''.join(i)
s=re.sub(r'\b[^a-zA-Z0-9]+\b',r' ',s)
print(s)

# Amostra de Entrada:
# 7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!