def solution(participant, completion):
    temp = {}
    for c in completion:
        if c in temp:
            temp[c] += 1
        else : temp[c] = 1

    for p in participant:
        if p in temp :
            val = temp[p]
            val -= 1
            if  val == 0: del temp[p]
            else : temp[p] = val
        else : return p

print(solution(["mislav", "stanko", "mislav", "ana", "sunho"], ["stanko", "ana", "mislav", "mislav"]))