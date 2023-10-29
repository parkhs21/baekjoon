formula = input()

precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
stack = []
postfix = ''

for c in formula:
    if c.isalpha():
        postfix += c
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
    else:
        while stack and stack[-1] != '(' and precedence[c] <= precedence[stack[-1]]:
            postfix += stack.pop()
        stack.append(c)

while stack:
    postfix += stack.pop()

print(postfix)
    