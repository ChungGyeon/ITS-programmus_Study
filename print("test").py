def solution(num, total):
    start = (total // num) - (num - 1) // 2
    answer = [start+i for i in range(num)]
    return answer

print(solution(3, 12))  
print(solution(5, 15))  
print(solution(4, 14)) 