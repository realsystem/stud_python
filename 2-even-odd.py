num = int(raw_input('number: '))
check = int(raw_input('check: '))
if not (num % 4):
    print 'multiple of 4'
elif num % 2:
    print 'odd'
else:
    print 'even'
if not num % check:
    print str(num) + ' div ' + str(check)
