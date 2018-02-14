def readfile(name):
    res = []
    with open(name, 'r') as t_file:
        line = t_file.readline()
        if line:
            res.append(line.strip())
        while line:
            line = t_file.readline()
            if line:
                res.append(line.strip())
    return res


if __name__ == '__main__':
    primes = readfile('primenumbers.txt')
    happys = readfile('happynumbers.txt')
    for p in primes:
        if p in happys:
            print p
