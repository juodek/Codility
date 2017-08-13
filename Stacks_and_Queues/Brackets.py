def solution(S):
    if len(S) == 0:
        return 1
    if len(S) % 2 == 1:
        return 0
    dict = { ')': '(', ']': '[', '}': '{'}
    stack = []
    for i in xrange(len(S)):
        if len(stack) == 0:
            stack.append(S[i])
        elif S[i] in dict and dict[S[i]] == stack[len(stack) - 1]:
            stack.pop()
        else:
            stack.append(S[i])
    return int(len(stack) == 0)
