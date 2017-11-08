def checkio(expression):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for char in expression:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if len(stack) == 0 or brackets.get(stack.pop()) != char:
                return False
    return len(stack) == 0
