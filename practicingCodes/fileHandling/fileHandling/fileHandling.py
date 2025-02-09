# for i in range(4):
#   for j in range(10):
#      if j<=10/2 and i<=4/2:
#         print('#');
#      elif j>10/2 and i>4/2:
#         print('-'); 

# Using for loop
for i in range(10):

	print(i, end=" ")

	# break the loop as soon it sees 6
	if i == 6:
		break

print()

# loop from 1 to 10
i = 0
while i < 10:

	# If i is equals to 6,
	# continue to next iteration
	# without printing
	if i == 6:
		i += 1
		continue
	else:
		# otherwise print the value
		# of i
		print(i, end=" ")

	i += 1

with open("file.txt", "r") as file:
    # data = file.read()
    # print (data)
    

   data = file.readlines()
  # print (data)
   for line in data:
     word = line.split('-')
     print (line)
     
# Python code to illustrate append() mode

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

file = open('file.txt', 'a')
file.writelines(L)
file.close()


# File Handling

import os

def create_file(filename):
	try:
		with open(filename, 'w') as f:
			f.write('Hello, world!\n')
		print("File " + filename + " created successfully.")
	except IOError:
		print("Error: could not create file " + filename)

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			contents = f.read()
			print(contents)
	except IOError:
		print("Error: could not read file " + filename)

def append_file(filename, text):
	try:
		with open(filename, 'a') as f:
			f.write(text)
		print("Text appended to file " + filename + " successfully.")
	except IOError:
		print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
	try:
		os.rename(filename, new_filename)
		print("File " + filename + " renamed to " + new_filename + " successfully.")
	except IOError:
		print("Error: could not rename file " + filename)

def delete_file(filename):
	try:
		os.remove(filename)
		print("File " + filename + " deleted successfully.")
	except IOError:
		print("Error: could not delete file " + filename)


if __name__ == '__main__':
	filename = "example.txt"
	new_filename = "new_example.txt"

	create_file(filename)
	read_file(filename)
	append_file(filename, "This is some additional text.\n")
	read_file(filename)
	rename_file(filename, new_filename)
	read_file(new_filename)
	delete_file(new_filename)


# Open a file for reading
file = open('file.txt', 'r')

# Read the first line of the file
line = file.readline()

# Loop through the rest of the file and print each line
while line:
	print(line)
	line = file.readline()

# Close the file when you're done
file.close()
