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

s = 'try     hello world'

print(solution(s))

# split을 사용할경우 공백이 여러개로 되어있을 경우 문제가 풀리지 않았다. -> 왜그런지 공부 필요