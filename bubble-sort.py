from util import execution_time, Sequence

@execution_time
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted =  False
        if already_sorted: 
            break
    return array
            
@execution_time
def run():
    seq = Sequence()
    it = iter(seq)
    prev = 0
    for i in range(0, 1000):
        t = next(it)
        if (prev != 0):
            prev = t
        tmp = [x for x in range(prev, t)]
        tmp.sort(reverse=True)
        bubble_sort(tmp)


if __name__ == '__main__':
    run()