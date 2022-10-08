from datetime import datetime as dt

def execution_time(function):
    def wrapper(*args, **kwargs):
        initial_time = dt.now()
        function(*args, **kwargs)
        final_time = dt.now()
        time_elapsed = final_time - initial_time
        print(" >> ", time_elapsed.total_seconds(), " seconds")
    return wrapper

""" 
Pseudocode for INSERTION SORT
for j = 2 to A.length
    key = A[j]
    // Insert A[j] into the sorted sequence A[1, j-1]
    i = j-1
    while 1>0 and A[i] > key
        A[i+1] = A[i]
        i = i-1
    A[i+1] = key
"""


@execution_time
def insertion_sort(seq):
    array = seq
    size = len(array)
    print(f'The size is {size}')
    # print(f'The original array is: {array}')
    for i in range(1, size):
        key = array[i]
        j = i - 1
        
        while (j >= 0 and array[j] > key):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    
    # print(f'The final array is: {array}')
    return array
    
class Sequence:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    

def run():
    seq = Sequence()
    it = iter(seq)
    prev = 0
    for i in range(0, 101):
        t = next(it)
        if (prev != 0):
            prev = t
        tmp = [x for x in range(prev, t)]
        tmp.sort(reverse=True)
        insertion_sort(tmp)
        # print(tmp)

if __name__ == '__main__':
    run()
    