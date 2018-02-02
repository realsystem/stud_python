inp = int(raw_input('Number for prime check: '))
cnt = 0
div = []
if inp == 1:
    cnt += 1
for i in range(2, inp):
    if not inp % i:
        cnt += 1
        div.append(i)
if cnt:
    print 'not prime'
    print div
else:
    print 'prime'
