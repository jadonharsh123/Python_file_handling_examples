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