from datetime import date
name = raw_input('enter your name: ')
age = int(raw_input('enter your age: '))
rpt = int(raw_input('counts: '))
year = 100 - age + date.today().year
for i in range(0, rpt):
    print('{}, your will be 100 year old in {}'.format(name, year))