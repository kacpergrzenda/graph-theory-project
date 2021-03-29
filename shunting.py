# Adapted from the pseudocode at:
#https://en.wikipedia.org/wiki/Shunting-yard_algorithm


def shunt(infix):
    """Convert infix expressions to postfix."""
    # The eventual output.
    postfix = ""
    # The shunting yard operator stack.
    stack = ""
    # operator precedence.
    prec = {'*': 100,'/': 90, '+': 80, '-': 70} 
    # loop through the input a cahracter at a time.
    for c in infix:
        # If c is a digit.
        if c in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            # Push it to the outpu.
            postfix = postfix + c
        # c is an operator.
        elif c in {'+', '-', '*', '/'}:
            # check what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Push c to stack.
            stack = stack + c
        elif c == '(':
            # Push c to stack.
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Remove open bracket from stack.
            stack = stack[:-1]
    while len(stack) != 0:
        # Append operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove operator from stack.
        stack = stack[:-1]
    return postfix

                
                

#check if i was running the commandline as script
if __name__ == "__main__":
    infix = "3+4*(2-1)"
    postfix = "3421-*+"
    print(f"{infix} - > {shunt(infix)}")
    print(f"shunt: {shunt(infix)}")
    print(f"postfix: {postfix}")
    if shunt(infix) == postfix:
        print ("Program works")

