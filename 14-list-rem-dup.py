import random


def gen_list(count=14, max_num=99):
    res = []
    i = 0
    while i < count:
        num = random.randint(0, max_num)
        if num not in res:
            res.append(num)
            i += 1
    return res

print gen_list(10, 10)
