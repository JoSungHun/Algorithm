def solution(heights):
    answer = []
    for i in range(len(heights)-1, -1, -1):
        print("i:{}".format(i))
        print("heights[i] : {}".format(heights[i]))
        if i == 0:
                answer.append(0)
                print("append 0")
                break
        
        for x in range(i-1, -1, -1):
            print("x:{}".format(x))
            print("heights[x] : {}".format(heights[x]))

            if (heights[x] > heights[i]):
                answer.append(x+1)
                print("append {}".format(x+1))
                break
            elif (x==0) and (heights[x] <= heights[i]):
                answer.append(0)
                print("append 0")
                break
            

    answer.reverse()
    return answer

heights = [0, 1, 1, 1]
answer = solution(heights)
print(answer)