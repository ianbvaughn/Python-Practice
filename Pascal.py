import math

def num_combinations(n,r):
 return int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r)))

def pascal_output(arr):
 output = []
 a = arr[0]
 b = arr[1]
 return num_combinations(a,b)

def pascal(n):
 triangle = []
 for i in range(0,int(n)):
  for j in range(0,i+1):
   triangle.append([i,j])
 return [pascal_output(n) for n in triangle]

a = input('Enter n:')

print(pascal(a))