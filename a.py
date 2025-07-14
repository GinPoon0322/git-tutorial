def operate(stack, op):
    numB = stack.pop()
    numA = stack.pop()

    if op == '+':
        stack.append(numA + numB)
    elif op == '-':
        stack.append(numA – numB)
    elif op == '*':
        stack.append(numA * numB)
    elif op == '/':
        stack.append(numA / numB)

stack = []
stack.append(10)
stack.append(5)
operate(stack, '/')
stack.append(2)
stack.append(3)
operate(stack, '*')
operate(stack, '+')
print(stack[0])
