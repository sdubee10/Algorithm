#30분

def solution(s):
    stack = []
    for alpha in s:
        if alpha == "(":
            stack.append(alpha)
        elif stack and alpha == ")":
            stack.pop()
        else:
            return False

    if len(stack) == 0:
        return True
    else:
        return False