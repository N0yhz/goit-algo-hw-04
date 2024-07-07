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