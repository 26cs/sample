# (01) Start.
print('Hello world!')

# (02) Variable.
message = 'Hello world!'
print(message)

# (03) String concatenation.
first_name = 'albert'
last_name = 'einstein'
full_name = first_name + ' ' + last_name
print(full_name)

# (04) Lists.
bikes = ['Trek', 'Giant', 'Redline']
first_bike = bikes[0]
last_bike = bikes[-1]
for bike in bikes:
    print(bike)

bikes2 = []
bikes2.append('Trek')
bikes2.append('Giant')
bikes2.append('Redline')

# (05) Numerical lists.
squares = []
for x in range(1, 11):
    squares.append(x ** 2)

# (06)
squares2 = [x ** 2 for x in range(1, 11)]

# (07)
finishers = ['sam', 'bob', 'ada', 'bea']
first_two = finishers[:2]

# (08)
copy_of_bikes = bikes[:]

# (09)
dimensions = (1920, 1080)

# (10)
if (x == 42):
    print('ok')
if (x != 42):
    print('ok, too')
if (x > 42):
    print('x > 42')
if (x >= 42):
    print('x >= 42')
if (x < 42):
    print('x < 42')
if (x <= 42):
    print('x <= 42')

# (11)
if ('Trek' in bikes):
    print('Has Trek.')
if ('Foo' not in bikes):
    print('Foo not in bikes.')

# (12)
age = 19
if age >= 18:
    print('You can vote.')

# (13)
ticket_price = 20;
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 10
else:
    ticket_price = 15
print('Ticket price = ' + str(ticket_price))

# (14)
game_active = True
can_edit = False

# (15) Dictionary.
alien = {'color': 'red', 'points': 5}

# (16) Get value from dictionary.
print("The alien's color is " + alien['color'])

alien['foo'] = 42

xx = {'eric': 17, 'ever': 4}
for name, number in xx.items():
    print(name + ' loves a number ' + str(number))
for name in xx.keys():
    print(name + ' --> ')
for n in xx.values():
    print(str(n) + ' is a favourite number.')

# (17) User input.
my_name = input("\nWhat's your name?\n")
print('Hello, ' + my_name)

my_age = input('\nHow old are you?\n')
my_age = int(my_age)

my_grade = input('\nWhat is your grade?\n')
my_grade = int(my_grade)

temp = input('\nWhat is your body\'s temperature?\n')
pi = float(temp)
