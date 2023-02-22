from collections import Counter
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    result = Counter(participant) - Counter(completion)
    answer = list(result)[0]

    
    return answer