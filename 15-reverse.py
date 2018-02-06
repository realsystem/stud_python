

def reverse(string):
    string_list = string.split()
    string_list.reverse()
    return string_list

user_string = raw_input('enter the string line: ')
print ' '.join(reverse(user_string))