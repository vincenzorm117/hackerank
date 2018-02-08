def is_matched(expression):
    stack = []
    acceptedCharacters = ['{','}','(',')','[',']']
    matching = {'[':']', '(': ')', '{': '}'}
    for s in expression:
        if s not in acceptedCharacters:
            return False
        if s == '[' or s == '{' or s == '(':
            stack.append(s)
        else:
            if 0 >= len(stack):
                return False
            peek = stack[len(stack)-1]
            if matching[peek] != s:
                return False
            stack.pop()
    return 0 == len(stack)
             

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
