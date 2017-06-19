import time #this is a Python library
def quicksort(L):
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
"""Implement in-place quick sort in Python.
Input a list.
Output a sorted list."""
def inline_quicksort(array):
    if array == None or len(array) < 2:
        return array
    front_index = 0
    pivot_index = len(array) - 1
#    back_index = pivot_index
    pivot = array[pivot_index]
    while front_index < pivot_index:
        if array[front_index] > pivot:
            array[pivot_index] = array[front_index]  #move larger element behind pivot
            pivot_index -= 1
            array[front_index]= array[pivot_index]  #move displace element to front
        else:
            front_index += 1

    return quicksort(array[0:pivot_index]) + [pivot] + quicksort(array[pivot_index+1:])



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
                fill(L,Right,j,k+1,end)
                return L

        else:
            L[k] = Right[j]
            j+= 1

            if j >= end-middle:
                #print("L before Left fill = ",L)
                fill(L,Left,i,k+1,end)
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
    print "inline_quicksort test"
    test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print inline_quicksort(test)

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



    print time_execution('quicksort(A)')
    print time_execution('quicksort(B)')
    print time_execution('quicksort(C)')
    print time_execution('quicksort(D)')
    print time_execution('quicksort(E)')
    print time_execution('quicksort(F)')

    test_cases = [[4,6,5,8,3,2,1,7],[1],[2,1,3],[2,1,2],list(range(1,101010)),list(range(1,100)+range(1,100))]
    lengths = []
    for i in range(0,len(test_cases)):
        lengths.append(len(test_cases[i]))
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
