def solution(s):
    p_num = 0
    y_num = 0

    for i in range(0, len(s)):
        if s[i] == "p" or s[i] == "P":
            p_num += 1
        elif s[i] == "y" or s[i] == "Y":
            y_num += 1
    if p_num == y_num:
        return True
    else:
        return False


s = "pPoooyY"
print(solution(s))

# 공부해야 할 것 : count, upper, lower 함수