#Gowtham
import sys, string, math
s0,s1 = input().split()
n0 = len(s0)
n1 = len(s1)
if n1 > n0 :
    i = 0
    while i<n0 and s0[i] == s1[i] :
        i += 1
    print(n1-i)
elif n1 == n0 :
    i = 0
    while i<n1 and s0[i] == s1[i] :
        i += 1
    print(n1-i)
else :
    i = 0
    while i<n1 and s0[i] == s1[i] :
        i += 1
    s31 = s0[i:]
    s32 = s1[i:]
    L = list(s31)
    k = 0
    for c in s32 :
        if c in L :
            k += 1
            L.remove(c)
    print(n0-i-k)
