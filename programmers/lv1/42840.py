def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    result = [0, 0, 0]
    for i in range(len(answers)):
        
        if answers[i] == one[i%len(one)]:
            result[0] += 1
        if answers[i] == two[i%len(two)]:
            result[1] += 1
        if answers[i] == three[i%len(three)]:
            result[2] += 1

    maxi = max(result)
    for a in range(0, len(result)):
        if result[a] == maxi:
            answer.append(a+1)

    
    return answer