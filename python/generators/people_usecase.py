import psutil
import random
import time

'''Significantly faster...and easier on memory.
Memory before every thing 14.1
Memory before list 14.1
Memory after list 22.5
List took 8.498840570449829 Seconds

Memory before generator 13.9
Memory after generator 13.9
Generator took 5.4836273193359375e-06 Seconds

It stops when it gets to yield statement.
'''

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print(f'Memory before every thing {psutil.virtual_memory().percent}\n')

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

print(f'Memory before list {psutil.virtual_memory().percent}')
t1 = time.time()
p = people_list(10_000_000)
t2 = time.time()
print(f'Memory after list {psutil.virtual_memory().percent}')
print('List took {} Seconds\n'.format(t2-t1))
del t1, p, t2
time.sleep(10)
print(f'Memory before generator {psutil.virtual_memory().percent}')
t1 = time.time()
p = people_generator(10_000_000)
t2 = time.time()
print(f'Memory after generator {psutil.virtual_memory().percent}')
print('Generator took {} Seconds'.format(t2-t1))
