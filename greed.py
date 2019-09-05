def score(dice):
    die = dict()
    score = {1:1000, 2:200, 3:300, 4:400, 5:500, 6:600}
    mini_score = {1:100, 5:50}
    for d in dice:
        die[d] = die.get(d,0) + 1
    s = [score[k] for k,v in die.items() if die[k] >= 3]
    for d in dice:
        if d not in [1, 5]: continue
        elif die[d] > 3:
            s.append((die[d]-3)*mini_score[d])
        elif die[d] < 3:
            s.append(die[d]* mini_score[d])
        else: pass
    return sum(s)


result = score([2, 4, 4, 5, 4])
print(result)
