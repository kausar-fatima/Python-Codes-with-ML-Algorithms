# python practicing codes
grade = int(input(('\nTask1************\nEnter your grades: ')));
if(grade>80):
    print('your grade is A');
else:
    print('Your grade is B');
    
print('\nTask2************\nLet us display eligible students for admission: \n');
name = ['fatima','fariha','fakhra'];
age = [20,26,18];
i = 0;
while(i<len(name)):
    if(age[i]<20):
        print(name[i]+' is eligible\n');
    else:
        print(name[i]+' is not eligible\n');
    i=i+1;
    
print('\nTask3************\nLet us display even numbers: \n');
j = 1;
while(j<20):
    if(j%2==0):
        print('\nEven number is: ',j);
    
    j=j+1;

print('\nTask4************\nLet us count a character in a line: \n');
stringline = input('Enter a line: ');
char = input('Enter a character: ')[0];

count = 0;
for character in range(len(stringline)):
    if(char==stringline[character]):
       count=count+1;
    

# print(stringline.count(char));
print('Number of count of '+str(char)+' is: '+ str(count));

count = 0;
name = input('Enter your name: ');
vowel = "aeiouAEIOU";
for char in name:
     if char in vowel:
        print(char,'\n');
        count=count+1;

print('Number of vowels are: ',str(count));

vowel = ['a','e','i'];
for char in name:
     if char in vowel:
        print(char,'\n');
        count=count+1;

print('Number of vowels are: ',str(count));