'''
We will take a list of large numbers and calculate their factorials. Calculating the factorial for each large number is time-consuming. To optimize, we will divide the numbers among multiple processes, allowing different CPU cores to work concurrently. This approach prevents a single core from being overloaded while others remain idle.
'''

import multiprocessing
import math
import sys 
import time

##increse the maximum number of digits for integer conversion


sys.set_int_max_str_digits(100000)

## function to computer  factorial of a given number

def compute_factorial(number):
    print(f"computeing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":

    ## define list of large number for factorial calcualteion

    numbers=[6000,7000,8000]

    # creating a pool of worker processes
    start_time=time.time()
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)
    ## end the time

    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time-start_time} seconds")

