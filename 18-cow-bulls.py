import random


def get_cows_and_bulls(a, b):
    l = []
    n = 0
    for i in range(0, 4):
        if a[i] == b[i]:
            l.append(i)
    for i in range(0, 4):
        if i not in l:
            if a[i] in b:
                n += 1
    return len(l), n


if __name__ == '__main__':
    comp_num = str(random.randrange(1000, 9999))
    print comp_num
    cnt = 1
    while cnt != 0:
        input_num = raw_input('Guess the 4-digit number: ')
        if input_num == 'exit' or input_num == '' or cnt > 99:
            print 'game over'
            break
        if input_num == comp_num:
            print 'you win'
            print 'cnt: ' + str(cnt)
            break
        cows, bulls = get_cows_and_bulls(input_num, comp_num)
        print 'cows: ' + str(cows) + ' bulls: ' + str(bulls)
        cnt += 1
