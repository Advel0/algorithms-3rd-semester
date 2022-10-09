import random
import time

def finished_sorting(file_name):
    counter = 1
    with open(file_name, 'rb') as file:
        prev_num = int(file.readline().decode()[:-1])
        for line in file:
            num = int(line[:-1])
            if num < prev_num:
                return False
            prev_num = num
    return True

def natural_merge_sort(file_name):
    while not finished_sorting(file_name):
        divide_file(file_name)
        natural_merge(file_name)


def divide_file(file_name):
    with open(file_name, 'rb') as file, open('B.bin', 'wb') as b_file, open('C.bin', 'wb') as c_file:
        counter = 0
        prev_num = int(file.readline().decode()[:-1])
        b_file.write((str(prev_num)+'\n').encode())

        for line in file:
            num = int(line.decode()[:-1])
            if prev_num > num:
                counter +=1

            if counter % 2 == 0:
                b_file.write((str(num)+'\n').encode())
            else:
                c_file.write((str(num)+'\n').encode())

            prev_num = num

        b_file.write('\n'.encode())
        c_file.write('\n'.encode())


def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line



def natural_merge(file_name):
    with open(file_name, 'wb') as file, open('B.bin', 'rb') as b_file, open('C.bin', 'rb') as c_file:

        b_file_end = False
        c_file_end = False 

        while not b_file_end or not c_file_end:
            
            if not b_file_end:
                b_num =  int(b_file.readline().decode()[:-1])
                b_seq_end = False
            if not c_file_end:
                c_num =  int(c_file.readline().decode()[:-1])
                c_seq_end = False
              

            while not b_seq_end or not c_seq_end:
                
                if b_num < c_num and not b_seq_end or c_seq_end:
                    
                    file.write((str(b_num)+'\n').encode())
                    if peek_line(b_file).decode() == '\n':
                        b_file_end = True
                        b_seq_end = True
                    elif b_num > int(peek_line(b_file).decode()[:-1]):
                        b_seq_end = True
                    else:
                        b_num = int(b_file.readline().decode()[:-1])
                elif not c_seq_end or b_seq_end:
                    
                    file.write((str(c_num)+'\n').encode())
                    if peek_line(c_file).decode() == '\n':
                        c_file_end = True
                        c_seq_end = True
                    elif c_num > int(peek_line(c_file).decode()[:-1]):
                        c_seq_end = True
                    else:
                        
                        c_num = int(c_file.readline().decode()[:-1])

def generate_file(file_name, size):
    with open(file_name, 'wb') as file:
        for i in range(size):
            file.write((str(random.randint(0,100034595439943453345345345354332342345300))+'\n').encode()) 


def presort(file_name):
    buff = []
    with open(file_name, 'rb') as file, open(file_name[:-4]+'_to_sort.bin', 'wb') as n_file:
        for line in file:
            if len (buff) > 7500000:
                buff.sort()
                for num in buff:
                    n_file.write((str(num)+'\n').encode())
                buff.clear()


            buff.append(int(line.decode()[:-1]))
        buff.sort()
        for num in buff:
            n_file.write((str(num)+'\n').encode())

generate_file('test.bin',25000000)
presort('test.bin')

t = time.time()
natural_merge_sort('test_to_sort.bin')
print(time.time() - t)