def generateParenthesis(n: int):
    res = []
    right, left = 0,0
    def backtrace(s, right, left):
        if len(s) == 2 * n:
            res.append(s)
            return
        if left < n:
            backtrace(s + "(", right, left + 1)
        if right < left:
            backtrace(s + ")", right + 1, left)

    backtrace("", 0, 0)
    return res

print(generateParenthesis(3))