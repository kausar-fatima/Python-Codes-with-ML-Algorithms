from tokenize import String

add_numbers = lambda x, y: x+y;

num1 = 20;
num2 = 5;

result = add_numbers(num1,num2);

print(result);

def factorialnum(num):
    if(num==1):
        return num;
    else:
        return factorialnum(num-1)*num;    


print(factorialnum(5));


# To check ArmStrong Number

numVal = 120;
val = numVal;
number = 0;
n = 0;
numList = [];

while(numVal!=0):
    n = n+1;
    numList.insert(0,numVal%10);
    numVal = (int)(numVal/10);

for element in numList:
    number = number + element**n;

if(number == val):
    print(str(val)+' is an ArmString Number.');
else:
    print(str(val)+' is not an ArmString Number.');    


integer_value = 7
formatted_string = '{:04}'.format(integer_value)

print(formatted_string)

def FibonaciNo(n):
    if(n<=0):
        return print('invalid number');
    elif(n==1):
        return 0;
    elif(n==2):
        return 1;
    else:
        FibonaciNo(n-1)+FibonaciNo(n-2);
