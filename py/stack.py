
def Initialise(stack, pointer):
    stack = []
    pointer = 0
    return stack, pointer

def AddToStack(stack, pointer, item):
    stack.append(item)
    pointer += 1
    return stack, pointer

def RemoveFromStack(stack, pointer):
    del stack[len(stack)-1]
    pointer -= 1
    return stack, pointer


stack = []
pointer = 0
item = "Marwan"
Initialise(stack, pointer)
AddToStack(stack, pointer, item)
AddToStack(stack, pointer, item)
RemoveFromStack(stack, pointer)

print(stack)