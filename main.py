from util import execution_time, Sequence

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

@execution_time
def run():
    array: int[int] = [21, 41, 59, 26, 41, 58]
    print(f'Original Array {array}')
    result = insertion_sort(array)
    print(f'Result Array {result}')

if __name__ == '__main__':
    run()