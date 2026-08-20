
# ZERODIVISION ERROR

a = 1
b = 0

try:
    avg = a / b
    print("The average score is:", avg)
except ZeroDivisionError:
    print("Error!")


# VALUE ERROR

b = 10
c = a + b
print("SUM is", c)
#there is value of "a" defined in this program.


# NameError

a = 10
print(b)  # NameError: name 'b' is not defined.


# IndexError

a = [10, 20] 
print(a[5])  # IndexError: list index out of range.


# FileNotFoundError (I/O Error)

f = open("abc.txt", "r") 
# FileNotFoundError: No such file or directory.


# SyntaxError 

print("Hello" 
# SyntaxError: unexpected EOF while parsing


# RuntimeError






