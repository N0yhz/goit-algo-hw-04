# goit-algo-hw-04
ДЗ Модуль 4

**1. Total/average salary**

``` 
  data = ['Alex Korp,3000 ',
         'Nikita Borisenko,2000',
         'Sitarama Raju,1000']

file_path = 'salaries.txt'

with open(file_path, 'w', encoding= 'utf-8') as file:
    for line in data:
        file.write(line + '\n')
    
def total_salary(path):
    try:
        with open(path, 'r', encoding= 'utf-8') as file:
            salaries = []
            for line in file:
                name, salary = line.strip().split(',')
                salaries.append(int(salary))

            total = sum(salaries)
            average = total/ len(salaries) if salaries else 0

            return total, average
    except FileNotFoundError:
        return 'File not found'
    except Exception as q:
        return f'Error:{q}'
    
result = total_salary(file_path)

if isinstance(result, tuple):
    print(f'Total salary: {result[0]}. Avarage salary: {result[1]}')
else:
    print(result)
```

**2. Cats (id, name, age)**

```
data = ['60b90c1c13067a15887e1ae1,Tayson,3',
'60b90c2413067a15887e1ae2,Vika,1',
'60b90c2e13067a15887e1ae3,Barsik,2',
'60b90c3b13067a15887e1ae4,Simon,12',
'60b90c4613067a15887e1ae5,Tessi,5'
]

file_path = 'cats.txt'

with open (file_path, 'w', encoding= 'utf-8') as file:
    for line in data:
        file.write(line + '\n')

def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding= 'utf-8') as file:
            for line in file:
                if line:
                    cat_id, name, age = line.split(',')
                    cat_info = {
                        'id':cat_id,
                        'name': name,
                        'age': int(age)
                    }
                    cats.append(cat_info)

    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print(f'Error: {e}')
    return cats

cats_info = get_cats_info(file_path)
print(cats_info)
```

**4. Assistant bot**

*Main.py*
```
from parse import parse_input
from actions import handle_command

if __name__ == '__main__':            
        print('welcome to the assistant bot!')
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        result = handle_command(command,args)
        print(result)
```

*Pase.py*

```
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
```

*Actions.py*

```
from parse import parse_input

def add_contacts(args, contacts):
    if len(args) != 2:
        return 'Invalid arguments. Usage: add [name] [newphone]'
    name, phone = args
    contacts[name] = phone
    return 'Contact added'

def change_contacts(args, contacts):
    if len(args) != 2:
        return 'Invalid arguments. Usage: add [name] [newphone]'
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f'Contact {name} phone has been updated to {new_phone}.'
    else:
        return 'Contact not found'

def show_phone(args, contacts):
    if len(args) != 1:
        return 'Invalid arguments. Use: change [name] [new phone]'
    name = args[0]
    if name in contacts:
        return f'{name} phone number is {contacts[name]}.'
    else:
        return 'Contact not found.'

def handle_command(command,args):
    contacts = {}

    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in {'close', 'exit'}:
            print('Bye')
            break
        elif command == 'hello':
            print('How can I help you ?')

        elif command == 'add':
            print( add_contacts(args,contacts))
        
        elif command == 'change':
            print (change_contacts(args,contacts))
        
        elif command == 'phone':
            print(show_phone(args, contacts) )
        else:
            return 'Unknown command.'
```
