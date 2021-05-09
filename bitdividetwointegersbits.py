Approach : Keep subtracting the divisor from the dividend until dividend becomes less than divisor. The dividend becomes the remainder, and the number of times subtraction is done becomes the quotient. Below is the implementation of above approach : 

filter_none
edit
play_arrow

brightness_4
# Python 3 implementation to Divide two
# integers without using multiplication,
# division and mod operator
 
# Function to divide a by b and
# return floor value it
def divide(dividend, divisor): 
 
    # Calculate sign of divisor i.e.,
    # sign will be negative only iff
    # either one of them is negative
    # otherwise it will be positive
    sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1
     
    # Update both divisor and
    # dividend positive
    dividend = abs(dividend)
    divisor = abs(divisor)
     
    # Initialize the quotient
    quotient = 0
    while (dividend >= divisor): 
        dividend -= divisor
        quotient += 1
     
     
    return sign * quotient
 
 
# Driver code
a = 10
b = 3
print(divide(a, b))
a = 43
b = -8
print(divide(a, b))
 
# This code is contributed by
# Smitha Dinesh Semwal
