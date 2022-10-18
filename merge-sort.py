from util import execution_time, Sequence

def mergeSort(array):
    if len(array) > 1:

        a = len(array)//2
        l = array[:a]
        r = array[a:]

        # Sort the two halves
        mergeSort(l)
        mergeSort(r) 

        b = c = d = 0

        while b < len(l) and c < len(r):

            if l[b] < r[c]:
                array[d] = l[b]
                b += 1
            else:
                array[d] = r[c]

                c += 1

            d += 1

        while b < len(l):
            array[d] = l[b]
            b += 1
            d += 1

        while c < len(r):

            array[d] = r[c]
            c += 1
            d += 1
    return array

@execution_time
def test1K(lista):
    return mergeSort(lista)
    
    

def run():
    for i in [1000, 2000, 3000, 4000, 5000]:
        tmp = [x for x in range(i, 0, -1)]
        print(f"size:{i}")
        tmp = test1K(tmp)

if __name__ == '__main__':
    run()
    print(mergeSort([7, 6, 5, 4, 3, 2, 1]))