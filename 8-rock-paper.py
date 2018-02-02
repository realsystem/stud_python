import random


def find_index(char, lst):
    for i in range(0, len(lst) + 1):
        if char == lst[i]:
            return i

print 'Welcome to the Rock-Paper-Scissors game!'
print 'rock beats scissors'
print 'scissors beats paper'
print 'paper beats rock'
tools = ['r', 'p', 's']
# r = 0 -> 2
# p = 1 -> 0
# s = 2 -> 1
player = 'start'
timeout = 0
while player not in tools:
    player = raw_input('Make your choice(r, p, s): ')
    if timeout > 5:
        break
    if player in tools:
        player_num = find_index(player, tools)
        print player_num
        comp = random.randint(0, 2)
        print comp
        if comp == player_num:
            print 'once again'
            player = 'start'
            timeout = 0
        elif ((comp == 0) and (player_num == 2)) or \
            ((comp == 1) and (player_num == 0)) or \
            ((comp == 2) and (player_num == 1)):
            print 'comp win'
        elif ((player_num == 0) and (comp == 2)) or \
            ((player_num == 1) and (comp == 0)) or \
            ((player_num == 2) and (comp == 1)):
            print 'player win'
    else:
        print 'Wrong choice'
    cont = raw_input('want again?(y/n): ')
    if cont == 'y':
        player = 'start'
        timeout = 0
    timeout += 1
