def get_num_of_4(sentence):
    cnt = 1
    num = 0
    for c in sentence:
        if c == ' ' and cnt == 5:
            num += 1
            cnt = 1
            continue
        if c == ' ':
            cnt = 1
            continue
        cnt += 1
    return num

print get_num_of_4('this is a good test but it is not good like can be, and now it is better')
