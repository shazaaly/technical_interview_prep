
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    openings = '({['

    stack = []
    for bracket in s:
        if bracket in openings:
            stack.append(bracket)
        if not stack:
            return False
        if bracket == ')' and stack[-1] == '(' or \
           bracket == '}' and stack[-1] == '{' or \
           bracket == ']' and stack[-1] == '[':
            stack.pop()
    return not stack
                  
            
print(isValid("()[]{}"))
print(isValid("([]{}"))
print(isValid("()[{}"))