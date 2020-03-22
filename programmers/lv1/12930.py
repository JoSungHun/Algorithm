def solution(s):
    answer = ''
    check = 0
    for i in range(0, len(s)):
        if s[i] == ' ':
            answer += s[i]
            check = 0
        elif s[i].isalpha:
            if check % 2 == 0:
                answer += s[i].upper()
                check += 1
            else:
                answer += s[i].lower()
                check += 1
        else:
            answer += s[i]
    
    return answer

s = '_try     hello wor_ld'

print(solution(s))