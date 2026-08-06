def mul(x,y):
  return x*y
def add(x,y):
  return x+y
def minus(x,y):
  return x-y 
def divide(x,y):
  if y==0:
    return '除數不能為0'
  else:
    return x/y
# 2 input,4 output
def operation1(x,y):
  mul=x*y
  add=x+y
  minus=x-y
  divide=x/y if y!=0 else '除數不能為0'
  return [mul,add,minus,divide]
def operation2(x,y):
  mul=x*y
  add=x+y
  minus=x-y
  divide=x/y if y!=0 else '除數不能為0'
  return mul,add,minus,divide

def test():
  print('Hello World!')
