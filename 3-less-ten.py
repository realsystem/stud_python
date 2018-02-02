a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = int(raw_input('less then: '))
print 'less 10:'
for i in a:
    if i < 10:
        print i
for i in a:
    if i < c:
        b.append(i)
if b:
    print b
