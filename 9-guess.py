import random

cnt = 0
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
while 1:
    player_num = raw_input('Guess the number[1-9]: ')
    if player_num == 'exit':
        break
    if player_num not in numbers:
        print 'wrong input, try again'
    else:
        player_num = int(player_num)
        if player_num in range(1, 10):
            comp_num = random.randint(1, 9)
            if player_num > comp_num:
                print 'too high'
            elif comp_num > player_num:
                print 'too low'
            else:
                print 'exactly right'
            cnt += 1
        else:
            print 'wrong range, try again'
print 'stat: ' + str(cnt)
