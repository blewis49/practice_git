def score(dice):
    die = dict()
    score = {1:1000, 2:200, 3:300, 4:400, 5:500, 6:600}
    for d in dice:
        die[d] = die.get(d,0) + 1
        s = [die[d].get(score[d]) for d in die if die[d] == 3]
        print(s)
        # if the number of 1's or 5's < 3:
        if die.keys() in [1, 5]:
            die.get(val, 0)
        # append to s 100 pts for each occurrence of a 1 in the die list
        # append to s 50 pts for each occurrence of a 5 in the die list
    return s


result = score([4, 4, 4, 3, 3])
print(result)
