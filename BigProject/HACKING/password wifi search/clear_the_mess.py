import profile
import os

a = int(input())
b = int(input())



for i in range(a,b):
    profile.delete(str(i),filename = True)
