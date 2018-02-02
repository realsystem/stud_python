import math


with open('dataset1.csv', 'r') as data_file1:
    data1 = data_file1.readlines()
data1 = data1[1:]
with open('dataset2.csv', 'r') as data_file2:
    data2 = data_file2.readlines()
data2 = data2[1:]
print data1
print data2
names1 = []
names2 = []
leg_lens = []
stride_lens = []
stances = []
diets = []
dino1 = []
dino2 = []
dino = []
dino_speeds = []
speeds = {}


def parse(string):
    string = string.strip('\n')
    pos = string.find(',')
    first = string[0: pos]
    old_pos = pos + 1
    pos = string.find(',', old_pos, len(string))
    second = string[old_pos: pos]
    old_pos = pos + 1
    third = string[old_pos: len(string)]
    return first, second, third

for elem in data1:
    name, leg_len, diet = parse(elem)
    names1.append(name)
    leg_lens.append(leg_len)
for elem in data2:
    name, stride_len, stance = parse(elem)
    names2.append(name)
    stride_lens.append(stride_len)
    stances.append(stance)
for name, leg_len in zip(names1, leg_lens):
    dino1.append(dict([('name', name), ('leg_len', leg_len)]))
print dino1
for name, stride_len, stance in zip(names2, stride_lens, stances):
    dino2.append(dict([('name', name), ('stride_len', stride_len), ('stance', stance)]))
print dino2
for i in dino1:
    for j in dino2:
        if i['name'] == j['name']:
            dino.append(dict([('name', i['name']), ('leg_len', i['leg_len']), ('stride_len', j['stride_len']), ('stance', j['stance'])]))
print dino
for i in dino:
    speed = (float(i['stride_len'])/float(i['leg_len']) - 1) * math.sqrt(float(i['leg_len']) * 9.8)
    if i['stance'] == 'bipedal':
        dino_speeds.append(dict([('speed', speed), ('name', i['name'])]))
print dino_speeds
speed_list = sorted([i['speed'] for i in dino_speeds], reverse=True)
print speed_list
for dino_speed in speed_list:
    for dino in dino_speeds:
        if dino['speed'] == dino_speed:
            print dino['name']
