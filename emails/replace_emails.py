import sys


def main():
    if len(sys.argv) < 3:
        print "Error: not enough parameters"
        print "Run: ./replace_emails.py <filename> <new_email>"
        filename = 'tmp'
        new_email = 'tmp@tmp.com'
    else:
        filename = sys.argv[1]
        new_email = sys.argv[2]
    with open(filename, 'r+') as f:
        pos = 0
        clean_size = 0
        for i in range(0, 10):
            try:
                orig_line = f.readline()
                if not orig_line:
                    break
                line = orig_line.replace('\n', ' ').replace('\r', '')
                print line
                at_pos = line.find('@')
                before_at = line[0: at_pos]
                l_blank_pos = before_at.rfind(' ')
                after_at = line[at_pos + 1: len(line)]
                r_blank_pos = after_at.find(' ')
                email = line[l_blank_pos + 1: at_pos + r_blank_pos + 1]
                new_line = line.replace(email, new_email) + '\n'
                print new_line
                old_pos = f.tell()
                #print old_pos
                f.seek(pos)
                #print f.tell()
                f.write(new_line)
                pos = f.tell()
                #print pos
                f.seek(old_pos)
                #clean_size += len(orig_line) - len(new_line)
            except IOError:
                print 'e'
        #print clean_size
        f.close()


main()
