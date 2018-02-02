def fibo(count=13):
    if not count:
        return []
    if count == 1:
        return [1]
    if count == 2:
        return [1, 1]
    res = [1, 1]
    for i in range(2, count):
        res.append(res[i - 1] + res[i - 2])
    return res

cnt = int(raw_input('How many fibo you need?: '))
print fibo(cnt)