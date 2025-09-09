## Mulitithreading

## when to use multi threading

### I/O Bound Task : tasks that spend more time waiting for I/O oeprations (e.g. file operaiton)
### Concurrent Execution: ehen you want to to improve the throughput of your application by 

import threading 
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"NUmber: {i}")
def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f"Letter: {letter}")

## Create 2 threads 

t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
t=time.time()

##start the Thead
t1.start()
t2.start()

### wait for thread to complete

t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)