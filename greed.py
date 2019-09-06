import random

def score(dice):
    print(dice)
    die = dict()
    score = {1:1000, 2:200, 3:300, 4:400, 5:500, 6:600}
    mini_score = {1:100, 5:50}
    for d in dice:
        die[d] = die.get(d,0) + 1
    s = [score[k] for k,v in die.items() if die[k] >= 3]
    for d in [1, 5]:
        if die.get(d, 0) != 0 and die[d] > 3:
            s.append((die[d]-3)*mini_score[d])
        elif die.get(d, 0) != 0 and die[d] < 3:
            s.append(die[d]* mini_score[d])
        else: pass
    print(s)
    return sum(s)


#result = score(random.sample(range(1, 7), 5))
result = score([1,1,1,1,4])
print(result)
