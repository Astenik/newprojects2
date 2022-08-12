'''this project generates 40000000 numbers in a file, and that file reservet not larger than 4GB memory space.'''
import random
new_file = open('rand_num', 'w')
lst = []
new_lst = []
for num in range(1, 100):
     lst.append(num)
for num1 in range(100, 201):
     new_lst.append(num1)
for num1 in range(1, 20000000):
     num = new_file.write(str(random.choice(new_lst)))
     num = new_file.write(' ')
     num = new_file.write(str(random.choice(lst)))
     num = new_file.write(' ')
