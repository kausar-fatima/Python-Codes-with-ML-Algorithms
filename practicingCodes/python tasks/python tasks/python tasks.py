# Task_1


# def calculateNetSalary(salary):
#     seven_percent = salary*0.07;
#     five_percent = salary*0.05;
#     net_salary = 0;
#     if(salary>=30000):
#       net_salary = salary-seven_percent;
#       print('\nAs your salary is greater than or equal to 30000 then deduction would be of',seven_percent,'Rs\nNet salary would be: ',net_salary,'Rs');
#     elif(salary>=20000):
#       net_salary = salary-five_percent;
#       print('\nAs your salary is greater than or equal to 20000 then deduction would be of',five_percent,'Rs\nNet salary would be: ',net_salary,'Rs');
#     elif(salary<2000):
#       net_salary = salary;
#       print('\nAs your salary is less than 20000 then there would be no deduction \nNet salary would be: ',net_salary,'Rs');
    
# usersalary = int(input('Enter your Salary: '));
# calculateNetSalary(usersalary);

# Task_2

def power(n,p=2):
   print('Output of',n,' power',p,' would be: ',n**p)
   

number = float(input('Enter number: '))
select = int(input('do you wanna to input power(1 for yes): '))
if(select==1):
   pow = int(input('Enter power: '))
   power(number,pow)
else:
   power(number)


# Task_3

def add(num1,num2):
   print('Addition of',num1,' and',num2,' is',num1+num2)
   
def subtract(num1,num2):
   print('Subtraction of',num1,' and',num2,' is',num1-num2)
   
def multiply(num1,num2):
   print('Multiplication of',num1,' and',num2,' is',num1*num2)
   
def divide(num1,num2):
   print('Division of',num1,' and',num2,' is',num1/num2)

def showCase():
   
   print('Arithmetic operations on two numbers\n')
   print('Enter two numbers: ')
   val1 = int(input('first number: '))
   val2 = int(input('second number: '))
   choice = 0;
   print('Following menu driven program is for performing arithmetic operations on two numbers: \n')
   print('1: To add two numbers\n')
   print('2: To subtraction two numbers\n')
   print('3: To multiplication two numbers\n')
   print('4: To divide two numbers\n')
   choice = int(input('Enter your choice: '))
   
   if(choice==1):
      add(val1,val2)
   elif(choice==2):
      subtract(val1,val2)
   elif(choice==3):
      multiply(val1,val2)
   elif(choice==4):
      divide(val1,val2)
   check = int(input('Do you wanna to continue(1 for yes and 0 for no): '))
   if(check==1):
      showCase()
      

showCase()
   

