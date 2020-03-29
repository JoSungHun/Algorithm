def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer += participant[i]
            break
            
    if answer == '':
            answer += participant[-1]
    
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

solution(participant, completion)