import math

def sum_dig_pow2(a, b):
    lst = []
    for num in range(a, b+1):
        if num//10 == 0 and num > 0: lst.append(num)
        for log in range(int(math.floor(math.log(b+1, 10)))):
            if (num//10 >= 10**log and num//10 < 10**(log+1)):
                if sum([int(n)**(i+1) for i, n in enumerate(str(num))]) != num: continue
                else: lst.append(num)
    return lst


result = sum_dig_pow2(1, 1475)  # [135, 175, 518, 598, 1306]
print(result)

# kata best practices solution, https://www.codewars.com/kata/5626b561280a42ecc50000d1/solutions/python
def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

def sum_dig_pow(a, b):
    return filter(filter_func, range(a, b+1))
