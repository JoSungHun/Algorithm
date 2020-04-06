def solution(array, commands):
    answer = []
    temp = []
    for x in range(0, len(commands)):
        i = commands[x][0]
        j = commands[x][1]
        k = commands[x][2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

a = solution(array, commands)
print (a)