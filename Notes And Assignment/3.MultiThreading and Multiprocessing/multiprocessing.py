## Processes the run in parallel

## cpu -bound Tasks - tasks that re heavy on cpu usage (e.g. mathematical computatioan,database)

## Parallel execution: multiple coreso of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'square : {i*i}')
def cube_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'cube : {i*i*i}')
if __name__=='__main__':
## Create  2 Processes
    t=time.time()
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)

    #start the process 
    p1.start()
    p2.start()

    ## wait for the process to complete

    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)
