import sys
import random


def rand_char():
    random.seed()
    return unichr(random.randrange(97, 122))


def rand_str(str_len):
    res_str = ''
    for n in range(0, str_len):
        res_str = res_str + rand_char()
    return res_str


def gen_email(email_len):
    return rand_str(random.randrange(1, email_len - 5)) +\
           '@' +\
           rand_str(random.randrange(1, email_len - 5)) +\
           '.' +\
           rand_str(3)


def gen_line(str_len, e_num):
    aaa = rand_str(random.randrange(1, str_len / 3))
    email = gen_email(str_len / 3)
    bbb = rand_str(random.randrange(1, str_len / 3))
    line = ['', '', '']
    n = random.randrange(0, 3)
    line[n] = email
    line[n - 1] = aaa
    line[n - 2] = bbb
    res_line = line[0] + ' ' + line[1] + ' ' + line[2]
    return res_line


def main():
    if len(sys.argv) < 5:
        print "Error: not enough parameters"
        print "Run: ./gen_emails.py <filename> <line_num> <line_len> <emails_num_per_line>"
        filename = 'tmp'
        line_num = 10
        line_len = 50
        emails_num = 2
    else:
        filename = sys.argv[1]
        line_num = sys.argv[2]
        line_len = sys.argv[3]
        emails_num = sys.argv[4]
    f = open(filename, 'w')
    for n in range(0, line_num):
        f.write(gen_line(line_len, emails_num) + '\n')
    f.close()

main()
