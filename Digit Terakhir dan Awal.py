#Function exponential
import math

def digitAwal(a,b):
    return a ** b

#to get the first digit of the calculation result
#gagal untuk disambungkan ke function
def firstDigit(n):
    while n >= 10:
        n = n / 10
    return int(n)

print(digitAwal(10,8)%9)
print(digitAwal(2,3))
print(digitAwal(6,3)//100)

def digitAkhir(a,b):
    return a ** b

print(digitAkhir(10,8)%100)
print(digitAkhir(2,3))
print(digitAkhir(6,3)//35)