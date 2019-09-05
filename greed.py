def score(dice):
    die = dict()
    score = {1:1000, 2:200, 3:300, 4:400, 5:500, 6:600}
    mini_score = {1:100, 5:50}
    for d in dice:
        die[d] = die.get(d,0) + 1
        s = [score[k] for k,v in die.items() if die[k] >= 3]
        # if the number of 1's or 5's < 3:
    for d in dice:
        if d == 1 and die[d] < 3:
            s.append(100*die[d])
        if d == 5 and die[d] < 3:
            s.append(50*die[d])
    return sum(s)


result = score([1, 1, 1, 1, 1])
print(result)
