import random


def gen_list(cnt, max_num=99):
    res = []
    i = 0
    while i < cnt:
        random.seed()
        number = random.randrange(0, max_num)
        if number not in res:
            res.append(number)
        else:
            continue
        i += 1
    return res


def find(num_to_search, list_where_to_search):
    found = 0
    if len(list_where_to_search) == 1 and num_to_search != list_where_to_search[0]:
        return found
    list_len = len(list_where_to_search)
    while not found:
        pos = list_len / 2
        if num_to_search == list_where_to_search[pos]:
            found = 1
        if num_to_search < list_where_to_search[pos]:
            return find(num_to_search, list_where_to_search[0: pos])
        if num_to_search > list_where_to_search[pos]:
            return find(num_to_search, list_where_to_search[pos: list_len])
    return found


if __name__ == '__main__':
    target_list = sorted(gen_list(100, 1000))
    print target_list
    num = int(raw_input('Number: '))
    if num in target_list:
        print 'Number ' + str(num) + ' is in the list'
    if find(num, target_list):
        print 'is in the list'
