def solution(arr):
    answer = 0
    count = len(arr)
    for i in arr:
        answer += i
    return answer/count