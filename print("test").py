def solution(common):
    common.sort()

    if common[1]-common[0] == common[2]-common[1]:
        return common[-1]+common[1]-common[0]
    elif common[1] /common[0] == common[2] /common[1]:
        return common[-1]*(common[1]//common[0])
    else:
        return 0
common = [10,20,30]
print(solution(common))
