tmp_str = raw_input('to check for palindrome: ')
str_len = len(tmp_str)
cnt = 0
for i in range(0, str_len/2 + 1):
    if tmp_str[i: 1] == tmp_str[str_len - i: 1]:
        cnt += 1
if cnt == str_len/2:
    print 'palindrome'
