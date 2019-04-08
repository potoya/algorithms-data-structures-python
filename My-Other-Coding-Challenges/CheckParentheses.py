def isBalanced(s):
    return solution( list(s) )

def solution(charArray):
    stack = []
    for c in charArray:
        if c == '(' or c == '[' or c == '{':
            # caso - paren operto
            stack.insert(0, c)
        else:
            # caso - paren chiuso
            if len(stack) > 0:
                p = stack.pop(0)
                if isCounterPart(c,p):
                    return False
            else:
                return False

    if len(stack) == 0:
        return True

#
#
def isCounterPart(c, p):
    if c == '(' and p == ')' or c == '[' and p == ']' or c == '{' and p == '}' :
        return True
    else:
        return False

if __name__ == '__main__':
    inputStr = "[(){}]"
    print( isBalanced(inputStr) )