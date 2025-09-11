## Mutithreading with thread Pool Executor

from concurrent.futures import ThreadPoolExecutor

import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

numbers=[1,2,3,4,5,52,45,65,1,4,5,4,5,5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_number,numbers)
for res in results:
    print(res)
