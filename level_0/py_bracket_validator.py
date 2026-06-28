def bracket_validator(s: str) -> bool:
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    open_ = set(brackets.values())

    for i in s:
        if i in open_:
            stack.append(i)
        elif i in brackets:
            if not stack or stack[-1] != brackets[i]:
                return False
            stack.pop()
        
    return len(stack) == 0

print(bracket_validator('()'))
print(bracket_validator('([)]'))