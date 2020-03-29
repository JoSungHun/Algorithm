def solution(n):
    answer = ''
    pattern = '수박'
    
    if n % 2 == 0:
        answer += pattern * int(n/2)
    else:
        answer += pattern * int(n/2)
        answer += pattern[0]
    
    return answer