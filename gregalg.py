import time as t
from multiprocessing import Pool
import numpy as np

def func(lines):
    max_gregs = ''
    count = 0
    for i in lines:
        linecount = i.lower().count('greg ')
        if linecount > count:
            count = linecount
            max_gregs = i

    return max_gregs

if __name__ == '__main__':

    start = t.time()

    # Open the file in greg mode
    with open('greg.txt') as file:
        lines = file.readlines()

    print(f'File read in {t.time()-start} Seconds')

    start = t.time()
    lines_2_0 = np.array_split(lines, 4)

    print(f'Array split in {t.time()-start} Seconds')

    start = t.time()
    with Pool(4) as p:
        result = p.map(func,lines_2_0)

    print(f'Computed gregs in {t.time()-start} Seconds')


    max_gregs = ''
    count = 0
    for i in result:
        linecount = i.count('greg')
        if linecount > count:
            count = linecount
            max_gregs = i

    print(max_gregs)

