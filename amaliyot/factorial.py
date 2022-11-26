from math import factorial


n = int(input('Sonni kiriting: '))
a = 1

for i in range(1, n+1):
  a = i * a

print(a)

print(factorial(5))