#宣告
def f1(x):
  return x**2+x+1
def f2(x,y):
  return x**2+y**2+1
def f3(begin, end):
  total=0
  for i in range(begin, end+1):
    total+=i
  return total

############
num1=f1(2)
print(f'num1={num1}')
num2=f2(2,3)
print(f'num2={num2}')
num3=f3(1,3)
print(f'num3={num3}')