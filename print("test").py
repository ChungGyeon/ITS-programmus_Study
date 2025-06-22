"""
어우 문제 길어
"""

def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2  # 순간이동(건전지 소모 없음)
        else:
            n -= 1   # 점프(건전지 소모 1)
            answer += 1
    return answer

print(solution(5))






