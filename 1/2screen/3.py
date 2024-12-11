def mul_to_int (a,b):
    c = a * b
    if (c//1)>=c:
        return(int(c))
    else:
        return(float(c))

num1 = 4.5
num2 =  3

print(type(mul_to_int(num1,num2)))
    
print(mul_to_int(num1,num2))    