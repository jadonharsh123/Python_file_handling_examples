#1. Write a Python program to read an entire text file.
with open("example.txt", "r") as file:
    content = file.read()
print(content)

# 2 .Write a program that counts lines and characters in a file. With your favorite text editor, code a Python module called mymod.py, which exports three top-level names:
#a) A countLines(name) function that reads an input file and counts the number of lines in it 
#b) A countChars(name) function that reads an input file and counts the number of characters in it 
#c) A test(name) function that calls both counting functions with a given input file¬name. 
#All three mymod functions should expect a filename string to be passed in.
#Now, test your module interactively, using import and name qualification to fetch your exports. 

# modeule : mymod.py
# def countLines(name):
#     '''Count the number of lines in a file'''
#     count=0
#     with open(name,'r') as file:
#         for line in file:
#             count +=1
#     return count

# def countchar(name):
#     '''count the number of characters in a file'''
#     with open(name,'r') as file:
#         data=file.read()
#     return len(data)

# def test(name):
#     '''call both function and display'''
#     lines = countLines(name)  
#     chars = countchar(name)

#     print("File:",name)
#     print("Number of lines",lines)
#     print("Number of characters:",chars)

import mymod
print(mymod.countLines("example.txt"))
print(mymod.countchar("example.txt"))
print(mymod.test("example.txt"))



#3. Test your mymod module from Exercise 2 interactively, by using from to load the exports directly, first by name, then using the from* variant to fetch every¬thing.
from mymod import countchar,countLines,test
print(countLines("example.txt"))
print(countchar("example.txt"))
print(test("example.txt"))

#Q4. #Now, add a line in your mymod module that calls the test function automati¬cally only when the module is run as a script, not when it is imported The line you add will probably test the value of __name__ for the string "__main__",. Import the module and test its functions interactively. 
def countLines(name):
    '''Count the number of lines in a file'''
    count=0
    with open(name,'r') as file:
        for line in file:
            count +=1
    return count

def countchar(name):
    '''count the number of characters in a file'''
    with open(name,'r') as file:
        data=file.read()
    return len(data)

def test(name):
    '''call both function and display'''
    lines = countLines(name)
    chars = countchar(name)

    print("File:",name)
    print("Number of lines",lines)
    print("Number of characters:",chars)

if __name__ == "__main__":
    test("example.txt")


# 5. Write a second module, myclient.py, which imports mymod and tests its functions; run myclient from the system command line. If myclient uses from to fetch from mymod, will mymod’s functions be accessible from the top level of myclient? What if it imports with import instead? Try coding both variations in myclient and test interactively, by importing myclient .
import mymod
filename="example.txt"

print("Lines",mymod.countLines(filename))
print("characters:",mymod.countchar(filename))
mymod.test(filename)

#6. Package imports. Finally, import your file from a package. Create a subdirectory called mypkg nested in a directory on your module import search path, move the mymod.py module file you created in exercises 2 or 4 into the new directory, and try to import it with a package import of the form: import mypkg.mymod.
import Mypackage.mymod
print(Mypackage.mymod.countchar("example.txt"))
      
print(Mypackage.mymod.countLines("example.txt"))

Mypackage.mymod.test("example.txt")


#7.   Experiment with module reloads: perform the tests in the changer.py example, changing the called function’s message and/or behavior repeatedly, without stopping the Python interpreter. Depending on your system, you might be able to edit changer in another window.
import changer as ch
# ch.printer()

import importlib
importlib.reload(ch)
ch.printer()



