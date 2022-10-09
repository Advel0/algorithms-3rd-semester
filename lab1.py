import random

def amount_of_sequences(file_name):
    counter = 1
    with open(file_name, 'rb') as file:
        prev_num = int(file.readline().decode()[:-1])
        for line in file:
            num = int(line[:-1])
            if num < prev_num:
                counter += 1

            prev_num = num
    return counter


def natural_merge_sort(file_name):
    while amount_of_sequences(file_name) > 1:
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

        b_num =  int(b_file.readline().decode()[:-1])
        c_num =  int(c_file.readline().decode()[:-1])

        b_seq_end = False
        c_seq_end = False 

        b_file_end = False
        c_file_end = False 

        while not b_file_end or not c_file_end:

            
            
            if b_seq_end and c_seq_end:
                b_seq_end = False
                c_seq_end = False

            if b_file_end or b_seq_end:
                file.write((str(c_num)+'\n').encode())
                continue
            if c_file_end or c_seq_end:
                file.write((str(b_num)+'\n').encode())
                continue

            if b_num < c_num:
                file.write((str(b_num)+'\n').encode())

                if peek_line(b_file).decode() == '\n':
                    b_file_end = True
                elif b_num > int(peek_line(b_file).decode()[:-1]):
                    b_seq_end = True
                else:
                    b_num = int(b_file.readline().decode()[:-1])
            
            else:
                file.write((str(c_num)+'\n').encode())
            
                if peek_line(c_file )== '\n':
                    c_file_end = True
                elif c_num > int(peek_line(c_file).decode()[:-1]):
                    c_seq_end = True
                else:
                    c_num = int(c_file.readline().decode()[:-1])


with open('test.bin', 'wb') as file:
    for i in range(1000000):
        file.write((str(random.randint(0,100034595439943453345345345354332342345300))+'\n').encode()) 



# print(amount_of_sequences('test.bin'))

# divide_file('test.bin')

# with open('B.bin', 'rb') as file:
#     print(file.readline().decode())

# with open('test.bin', 'rb') as file:
#         for line in file:
#             print(line)

# file = open('B.bin','rb')

# print(peek_line(file))

# divide_file('test.bin')


# natural_merge_sort('test.bin')