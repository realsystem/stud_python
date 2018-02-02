num = int(raw_input('number: '))
res = []
for i in range(1, num + 1):
    if not num % i:
        res.append(i)
print res
