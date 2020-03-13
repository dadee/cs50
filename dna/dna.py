import csv
from sys import argv

#RUN AWAY! SPAGHETTY DETECTED!
#to run use >>> dna.py databases/small.csv sequences/2.txt

def get_dnas(file_db):  # getting row of target DNAs
    with open(file_db) as f:
        l = list(f.readline().replace('\n', '').split(','))
        l.pop(0)
    return l


def get_rows_number(file):  # getting number of rows in file. -not in use-
    with open(file) as f:
        r = sum(1 for row in f)
    return r


def get_seq(file_s):  # getting sequence
    with open(file_s) as f:
        l = f.readline().replace('\n', '')
        l += '00000'
    return l


def count_dna(dna, sequence):  # count nucleotids in sequence
    temp_counter = {x: 0 for x in dna}
    counter = {x: 0 for x in dna}
    for agat in dna:
        lenn = len(agat)
        for i in range(0, len(sequence) - lenn):
            seqseq = sequence[i:i + lenn]
            seqseq2 = sequence[i + lenn:i + lenn + lenn]
            if seqseq == agat:
                if seqseq2 == agat:
                    temp_counter[agat] += 1
                else:
                    if counter[agat] < temp_counter[agat]:
                        counter[agat] = temp_counter[agat]
                        temp_counter[agat] = 0
    for x in counter:
        counter[x] += 1
    return counter


def get_name_base(dbs):  # getting base of names and nucs from csv file
    names_array = {}
    with open(dbs, 'r') as f:
        reader = csv.reader(f)
        for i, value in enumerate(reader):
            names_array.update({value[0]: value[1:]})
    return names_array


def get_dna_name(result, names_array):  # getting name whom nucls are
    name = [k for k, v in names_array.items() if v == result]
    try:
        return name[0]
    except:
        return 'No match'


if (len(argv) != 3):
    print('two files needed as args')
    exit(1)

file_dbs = argv[1]
file_seq = argv[2]

dnas = get_dnas(file_dbs)
seqo = get_seq(file_seq)

res = count_dna(dnas, seqo)
res_list = [*res.values()]
res_list = [str(i) for i in res_list]
name_base = get_name_base(file_dbs)
name = get_dna_name(res_list, name_base)
print(name)
