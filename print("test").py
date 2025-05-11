# 앞놈을 잡고, 뒤까지 쭉 조사한 뒤 조건에 맞으면 같이 보내고 아니면 안보내는 형태로
def solution(people, limit):
    cnt=0
    sml=0
    big=len(people)-1
    people.sort()
    while(sml<=big):
        if(people[sml]+people[big]<=limit):
            sml+=1
        big-=1
        cnt+=1
    return cnt
        
    
            
people = [100, 200, 150, 80]  
limit=200
print(solution(people,limit))


"""
def solution(people, limit):
    cnt=0
    sum=people.pop(0)
    for i in people:
        if(sum==limit):
            cnt+=1
            sum=0
        if((sum+i)<=limit):
            sum+=i
            people.remove(i)
    if(people):
        cnt+=1
        return solution(people,limit)+cnt
    else:
        return cnt+1
"""

            





    