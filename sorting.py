import time
import math
import random
def counting_sort(array, max_value):
    """run_time O(n) when max_val =~ len(array).  Array contents integers
    betwen 0 & max_value. Returns sorted array. Preserves order of equal values
    (stable sort) by using array length plus max_value extra space."""
    n = len(array)  # number of elements in array
    if n < 2:
        return array
    counts = [0 for _ in range(max_value+1)]
    output_array = [None for _ in range(n+1)]
    for i in range(n) :
        counts[array[i]] += 1  #count occurences of inputs
    for i in range(1,max_value+1):
        counts[i] += counts[i-1]  #add number of entries smaller than current value
    for i in range(n-1,-1,-1):
        output_array[counts[array[i]]] = array[i]  #place value in appropriate position of output array
        counts[array[i]] -= 1  #ensure duplicate values go into empty slot in output
    return output_array

def quicksort(L):
    """Recursive sort using additional space"""
    middle= len(L)/2
    if middle < 1 :
        return L
    pivot = L[middle]
    left = []
    right = []
    for item in L[0:middle]+L[middle+1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return quicksort(left) + [pivot] + quicksort(right)

def inline_quicksort(array):
    """Sorts array in place"""

    if array == None or len(array) < 2:
        return
    quick_sort(array, 0, len(array) - 1)

def quick_sort(array, start, end):
    if len(array) < 2 or start > end:
        return
    front_index = start
    back_index = end
    pivot_value = array[back_index]
    while front_index < back_index:
        if array[front_index] > pivot_value:
            #value larger than pivot_value so swap
            array[back_index] = array[front_index]
            back_index -= 1
            array[front_index] = array[back_index]
        else:
            front_index += 1
    array[front_index] = pivot_value  #insert pivot into array
    quick_sort(array,start,front_index-1) #sort smaller values
    quick_sort(array,front_index+1, end) #sort larger values

def qsort(array):
    """ In-place quicksort using random pivot"""
    if array == None or len(array) < 2:
        return
    q_sort(array,0,len(array)-1)
def partition(array, left_index, right_index):
    pivot = array[random.randint(left_index,right_index)]
    while left_index < right_index:
        while array[left_index] < pivot:
            left_index += 1  #find value larger than pivot if any
        while array[right_index] > pivot:
            right_index -= 1 #find value smaller than pivot if any
        if left_index >= right_index:
            break
        array[left_index],array[right_index] = array[right_index],array[left_index]
        left_index += 1
        right_index -= 1
    if left_index == right_index:
        left_index += 1
    return left_index
def q_sort(array, left, right):
    index = partition(array, left, right)
    if left < index - 1:
        q_sort(array, left, index - 1)
    if index < right:
        q_sort(array, index, right)


def fill(L,Sorted,i,begin,end):
    #print Sorted,i,begin,end
    for output_index in range(begin,end+1): #copy remainder of array with remaining elements into output array
        L[output_index] = Sorted[i]
        i += 1
    return
def merge(L,begin,middle,end):
    Left = []
    for i in range(begin,middle+1):
        Left.append(L[i])
    #print ("Left = ",Left)
    Right = []
    for i in range(middle+1,end+1):
        Right.append(L[i])
    #print ("Right = ",Right)
    i = 0 #Left index
    j = 0 #Right index
    for k in range(begin, end + 1):
        if Left[i] < Right[j]:
            L[k] = Left[i]
            i += 1

            if i > middle-begin:
                #print("L before Right fill = ",L)
#                fill(L,Right,j,k+1,end)
                return L

        else:
            L[k] = Right[j]
            j+= 1

            if j >= end-middle:
                #print("L before Left fill = ",L)
                fill(L,Left,i,k+1,end)
                return L
def merge_sort(L):
    begin = 0
    end = len(L) - 1
    middle = (begin + end)/2
    if middle < end:
        mergesort(L,begin, middle)
        mergesort(L,middle+1,end)
        merge(L,begin,middle,end)
    return L
def time_execution(code):
   start = time.clock()  # start the clock
   result = eval(code)  # evaluate any string as if it is a Python command
   run_time = time.clock() - start  # find difference in start and end time
   return result, run_time  # return the result of the code and time taken

def mergesort(L,begin,end):
    middle = (begin + end)/2
    #print("middle = %d begin = %d end = %d")%(middle,begin,end)
    if middle < end:
        mergesort(L,begin, middle)
        mergesort(L,middle+1,end)
        merge(L,begin,middle,end)
    return L
if __name__ == '__main__':
    input = [7,2,5,3,3,7,5,3,8,2,14,13]
    empty = []

    print "inline_quicksort test"
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    inline_quicksort(test)
    print test
    A = [4,6,5,8,3,2,1,7]
    qsort(A)
    print A
    a = [26, 8, 40, 73, 60, 94, 28, 30, 88, 30, 9, 85, 61, 20, 45, 69, 2, 46,
    47, 60, 25, 31, 8, 5, 59, 54, 94, 86, 53, 20, 77, 65, 87, 14, 22]
#    inline_quicksort(a)
    qsort(a)
    print(a)

    A = [4,6,5,8,3,2,1,7]
    B = [1,2,3,4,5,6,7,8,9]
    C = [8,7,9,6,1,5,4,2,3]
    D = list(range(100,0,-1))
    E = list(range(1,101))
    F = list(range(1,100)+range(1,100))
    #print quicksort(A)
    #print A
    print mergesort(A,0,len(A)-1)

    print mergesort(C,0,len(C)-1)
    print mergesort(D,0,len(D)-1)
    print mergesort(input,0,len(input)-1)
    print merge_sort(A)

    print merge_sort(C)
    print merge_sort(D)
    print merge_sort(input)
    print merge_sort(F)



    print time_execution('quicksort(A)')
    print time_execution('quicksort(B)')
    print time_execution('quicksort(C)')
    print time_execution('quicksort(D)')
    print time_execution('quicksort(E)')
    print time_execution('quicksort(F)')

    test_cases = [[4,6,5,8,3,2,1,7],[1],[2,1,3],[2,1,2],list(range(1,101010)),list(range(1,100)+range(1,100))]
    lengths = [len(i) for i in test_cases]
    qsresults = []
    msresults = []

    for i in range(0,len(test_cases)):
        qsresults.append(time_execution('quicksort(test_cases[i])'))
        msresults.append(time_execution('mergesort(test_cases[i],0,lengths[i]-1)'))
    #print qsresults
    #print msresults
    print "quicksort times"
    for each in qsresults:
        print each[1]
    print "mergesort times"
    for each in msresults:
        print each[1]
