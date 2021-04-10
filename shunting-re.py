# Adapted from the pseudocode at:
#https://en.wikipedia.org/wiki/Shunting-yard_algorithm


def shunt(infix):
    """Convert infix expressions to postfix."""
    # The eventual output.
    postfix = ""
    # The shunting yard operator stack.
    stack = ""
    # operator precedence.
    prec = {'*': 100,'.': 90, '|': 80} 
    # loop through the input a cahracter at a time.
    for c in infix:
        # If c is a digit.
        # c is an operator.
        if c in {'*', '.', '|'}:
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
        else:
            # Push c to stack.
            postfix = postfix + c
    while len(stack) != 0:
        # Append operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove operator from stack.
        stack = stack[:-1]
    return postfix

                
                

#check if i was running the commandline as script
if __name__ == "__main__":
    for infix in ["a.(b.b)*.a", "1.(0.0)*.1"], "*dog":
        # infix = "3+4*(2-1)"
        # postfix = "3421-*+"
        print(f"{infix} - > {infix}")
        print(f"postfix: {shunt(infix)}")
   
