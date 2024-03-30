#Part 1
## Input and Output
name_0 = input('What is your name?')
print(f'Hello {name_0}')

## Data types
x = int(input('X value: '))
y = int(input('Y value: '))
z = x + y
print(z)

## Functions
def main():
    name_1 = input('Whats your name?')
    hello(name_1)

def hello(to = 'World'):
    print('Hello', to)

main()

# Part 2
## Conditions (Booleans)
a = int(input('A value: '))
b = int(input('B value: '))

if a < b:
    print('A < B')
elif a > b:
    print('B > A')
else:
    print('A == B')

score = int(input('Score:'))

if score >= 90 and score <= 100:
    print('Grade A')
elif score >= 80 and score <= 90:
    print('Grade B')
elif score >= 70 and score <= 80:
    print('Grade C')
elif score >= 60 and score <= 70:
    print('Grade D')
elif score >= 50 and score <= 60:
    print('Grade E')
else:
    print('Grade F')

## Match/Case
name_3 = input('Whats your name? ')

match name_3:
    case 'Harry' | 'Herminone':
        print('Gryffindor')
    case 'Draco':
        print('Slytherin')
