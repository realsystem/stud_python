import random


def rand_char(complexity):
    random.seed()
    chr_seq = range(65, 91) + range(97, 123)
    if complexity == 2:
        chr_seq = chr_seq + range(48, 58)
    if complexity == 3:
        chr_seq = chr_seq + range(48, 58) + range(33, 48) + range(58, 65) + range(91, 97) + range(123, 127)
    chr_seq.sort()
    return unichr(random.choice(chr_seq))


def rand_str(str_len, complexity):
    res_str = ''
    for n in range(0, str_len):
        res_str = res_str + rand_char(complexity)
    return res_str


def user_input(msg, max_num):
    inp = raw_input(msg)
    if inp == 'exit':
        return 0
    res = int(inp)
    if res in range(1, max_num + 1):
        return res


def main():
    while 1:
        pass_len = user_input('Password length: ', 255)
        if not pass_len:
            break
        complexity = user_input('Password complexity: ', 3)
        if not complexity:
            break
        print rand_str(pass_len, complexity)


main()
