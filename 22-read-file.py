names = []
with open('nameslist.txt', 'r') as t_file:
    line = t_file.readline()
    if line:
        names.append(line.strip())
    while line:
        line = t_file.readline()
        if line:
            names.append(line.strip())
print names
names_cnt = {}
for name in names:
    cnt = 0
    for n in names:
        if name == n:
            cnt += 1
    names_cnt[name] = cnt
print names_cnt
