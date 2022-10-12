# Write a Python function called max_num()to find the maximum of three numbers.
from math import factorial


def max_num(num1,num2,num3):

    max_list = [num1,num2,num3]

    return max(max_list)



# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(list):
    prev_val = 1
    for x in list:
        prev_val = prev_val * x
    
    print(prev_val)



# Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1]



# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(num, beg, end):
    if beg >= end:
        print('Make sure the beginning value is less than the ending value') 
    elif num >= beg and num <= end:
        print(f"{num} is within the range of {beg}-{end}")

    else: 
        print(f"{num} is not within range")





# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
def pascal(n):
    
    for x in range(n):
        for i in range(n-x+1):
           print(end=" ")

        for i in range(x+1):
            print(factorial(x)//(factorial(i)*factorial(x-i)), end=" ")

        print('\n')    
          
    



# Calling the max_num function inside of print because the max_num function is set to return a value not print it. Either way, the function operates as it should.
print(max_num(2,10,3))

#Calling the mult_list function. This function initializes prev_val as 1 because it it 
# assumed we would never multiply by 0. Meaning, to first iteration of the loop will multiply by 
# 1 to set the prev_val to the first value of the list.
mult_list([2,2,2])

# Calling the rev_string function inside a print function because I set the rev_string function to return the value, not print it. 
print(rev_string('hello'))

num_within(200,199,200)

pascal(5)