user='admin'
passw='admin'

def validation():
  ''' This function validates and decides whether to give access or not'''
  i=1
  while i>=1:
    name=input('enter your username')
    pw=input('enter your password')
    if name=='admin' and pw=='admin':
      print('Access approved')
      i=0
    else:
      print('Access denied. Please try again')
      
def sum(x,y):
  '''this function takes two parameters and adds them'''
  return x+y
def subtract(x,y):
  '''this function takes two parameters and subtracts them'''
  return x-y
def product(x,y):
  '''this function takes two parameters and multiplies them'''
  return x*y
def divide(x,y):
  '''this function takes two parameters and divides them'''
  return x/y

def average():
  '''this function asks the user for marks in 5 subjects, calculates the total
      and displays the average'''
  sub1=int(input('Enter the marks of first subject'))
  sub2=int(input('Enter the marks of second subject'))
  sub3=int(input('Enter the marks of third subject'))
  sub4=int(input('Enter the marks of fourth subject'))
  sub5=int(input('Enter the marks of five subject'))
  total=sub1+sub2+sub3+sub4+sub5
  avg=total/5
  return avg
def main():
  print("Welcome to Saksham's program. Please login to use the services")
  validation()
  serve=int(input("Enter 1 to use calculator and 2 to use average marks calculator"))
  if serve==1:
    type=int(input("enter 1 to add,2 to subtract ,3 to multiply and 4 to divide any two integers"))
    a=int(input('enter first number'))
    b=int(input('enter second number'))
      
    if type==1:
      result=sum(a,b)
      print('The sum is ',result)
      
    elif type==2:
      result=subtract(a,b)
      print('The subtraction is ',result)
    elif type==3:
      result=product(a,b)
      print('The product is ',result)
    elif type==4:
      result=float(divide(a,b))
      print('The division is ',result)
    else:
      print('Invalid operation')
  elif serve==2:
    result=average()
    print('The average marks is ',result)
  else:
    print('Sorry invalid service')
main()
              
      
  



