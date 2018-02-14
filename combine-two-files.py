def readfile(file_path):
    f = open(file_path, 'r')
    eof = 1
    food_list = []
    while eof:
        l = f.readline()
        food_list.append(l.strip())
        if not l:
            eof = 0
    return food_list


en_food_list = readfile('/Users/segorov//FOOD')
ru_food_list = readfile('/Users/segorov//FOOD_ru')
print en_food_list[0]
print ru_food_list[0]
if len(en_food_list) == len(ru_food_list):
    len_list = len(en_food_list)
else:
    print 'Error: bad len'
    exit(-1)
for i in range(0, len_list):
    print en_food_list[i] + ':' + ru_food_list[i]
