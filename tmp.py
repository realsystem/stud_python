def last2(str):
        count = 0
        start = 0
        while str[start: len(str) - 2] != '':
            print 'start: ', start
            print 'str: ', str[start: len(str) - 2]
            print 'sub: ', str[-2:]
            res = str.find(str[-2:], start, len(str) - 2)
            print 'res: ', res
            if res >= 0:
                count += 1
                start = res + 1
            else:
                start = len(str) - 2
            print 'count: ', count
        return count
print last2('xxxx')
