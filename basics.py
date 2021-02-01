# Kacper Grzenda
# Python basics
# 2021-01-30

#Function
def facotrial(n):
    """ Number to calculate factorial of."""
    #Deal with negative inputs
    if n < 1:
        m = -n
    else:
        m = n
    
    #the running total - eventually the factorial
    total = 1
    #Loop to do the multiplications
    while m > 0:
        total = total * m
        m = m - 1
    # Return the answer.
    if n < 1:
        return -total
    else:
        return total

#test the function
n = -20
# Calculate the factorial of n.
print(f"The factorial of {n} is {facotrial(n)}.")

#Practice code collatz conjecture
