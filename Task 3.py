def numbers(x, y):
    if y == str(65):
        return(True)
    elif x == str(65):
        return(True)
    elif 'x + y' == str(65):
        return(True) 
    else:
        return(False)    
x, y = input("Enter two numbers:").split()
result = numbers(x, y)
print(result)











    

    
