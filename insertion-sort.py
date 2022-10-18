from util import execution_time, Sequence

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
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while (j >= 0 and array[j] > key):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def run(n):
    seq = Sequence()
    it = iter(seq)
    prev = 0
    for i in range(0, n):
        t = next(it)
        if (prev != 0):
            prev = t
        tmp = [x for x in range(prev, t)]
        tmp.sort(reverse=True)
        return tmp
        

def test():
    for i in [1000, 2000, 3000, 4000, 5000]:
        tmp = run(i)
        print(tmp)
        
        # print(tmp)

if __name__ == '__main__':
    test()
    