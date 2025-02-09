#Task 1
class Student:
    
  def __init__(self,name,rollno):
    self.name=name
    self.rollno=rollno
s1 = Student("fatima",25)
print(s1.name)
print(s1.rollno) 

class Student:
  def __init__(self,name,rollno):
    self.name = name
    self.rollno = rollno
    
  def display(self):
    print("The Name of Student is: ",self.name)
    print("The roll no is: ",self.rollno)
    
obj=Student("fatima",25)
obj.display()


#Task2 
class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        index = len(self.stack) - 1
        while index >= 0 and item < self.stack[index]:
            index -= 1
        self.stack.insert(index + 1, item)
        
    #def ascend(self,item):
    def sort_descend(self):
        self.stack = sorted(self.stack, reverse=True)
    
    def pop(self):
        if len(self.stack)<1:
            return None
        return self.stack.pop()

    def display(self):
        print(self.stack)
        
    def size(self):
        return len(self.stack)
    
    
s1 = Stack()
s1.push(1)
s1.push(5)
s1.push(2)
s1.push(4)
s1.push(11)
s1.push(99)
s1.push(53)
s1.push(10)
print(s1.size())


print("Elements pushed in ascending order:")
s1.display()
print("Elements pushed in descending order:")
s1.sort_descend()
s1.display()

for i in range(7):
    popped_item = s1.pop()
    if popped_item is not None:
        print("Popped:", popped_item)
    s1.display()


#Task 3
class Queue:
    def __init__(self):
        self.queue=[]
        
    def enqueue(self,item):
        self.queue.append(item)
        
    def dequeue(self,item):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)
        
    def size(self):
        return len(self.queue)
    
    def search(self, y):
        if y in self.queue:
            print("Number found")
        else:
            print("Number not found")
    
    
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

y = int(input("Enter a number to search: "))
q.search(y)

q.dequeue(3)
print("After removing an element:")
q.display()
