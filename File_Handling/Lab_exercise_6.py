#1.  Write a Python program to read first n lines of a file.
file=open("example.txt")
lines = file.readlines()
n=int(input("Enter number of lines:"))
for i in range(n):
    print(lines[i])
file.close()

#2. Write a Python program to append text to a file and display the text.
file = open("example.txt","a")
text=input("Enter text to append: ")
file.write(text + "\n")
file.close()
file=open("example.txt","r")
print(file.read())

#3. Write a Python program to read a file line by line and store it into a list.
file = open("example.txt","r")
lines = [line.strip() for line in file]
print(lines)
file.close()

#4.  Write a program to print each line of a file in reverse order.
file = open("example.txt","r")
for line in file:
    print(line[::-1])
file.close()

#5. Write a Python program to write a list content to a file.
data = ["apple","banana","mango","orange"]
file = open("example.txt","w")
for item in data:
    file.write(item + "\n")
file.close()

#6. Write a program to compute the number of characters, words and lines in a file.
file = open("example.txt")
text = file.read()

characters = len(text)
words = len(text.split())
lines = len(text.split("\n"))

print("characters:",characters)
print("Words:",words)
print("Lines:",lines)


#7. Write a program to accept string/sentences from the user till the user enters “END” to. Save the data in a text file and then display only those sentences which begin with an uppercase alphabet. 
file = open("example.txt")
s = input("Enter sentences: ")
while s!="END":
    file.write(s + "\n")
    s=input("enter sentence:")
file.close()

file = open("example.txt","r")

for line in file:
    if line[0].isupper():
        print(line)
file.close()


#8. Write a program to enter the following records in a binary file: 
#Item No 	integer 
#Item_Name 	string 
#Qty 		integer 
#Price 		float 
#Number of records to be entered should be accepted from the user. Read the file to display the records in the following format: 
#Item No: 
#Item Name : 
#Quantity: 
#Price per item: 
#Amount: 	( to be calculated as Price * Qty)
import pickle

f = open("items.dat","wb")

n = int(input("Enter number of records: "))

for i in range(n):
    itemno = int(input("Item No: "))
    name = input("Item Name: ")
    qty = int(input("Quantity: "))
    price = float(input("Price: "))
    
    pickle.dump([itemno,name,qty,price],f)

f.close()

f = open("items.dat","rb")

try:
    while True:
        r = pickle.load(f)
        print("Item No:",r[0])
        print("Item Name:",r[1])
        print("Quantity:",r[2])
        print("Price per item:",r[3])
        print("Amount:",r[2]*r[3])
        print()
except:
    pass

f.close()

