def solution(babbling):
    babbling_dict = ["aya", "ye", "woo", "ma"]
    answer = 0
    for word in babbling:
        for babble in babbling_dict:
            if babble in word:
                word = word.replace(babble, " ")
        if len(word.strip()) == 0:
            answer += 1

    return answer

babbling_dict = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
print(solution(babbling_dict))

