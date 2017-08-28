""" Move non-zeros to the start of the array in as few writes as possible
[1, 0, 3, 1, 2, 0, 5, 0] => [1, 1, 3, 5, 2, ?, ?, ?]
"""
def removeZeros(arr):

    start_index = 0
    end_index = len(arr) - 1
    while start_index < end_index:
        if arr[start_index] != 0:
            start_index += 1
        else:
            while arr[end_index] == 0 and end_index > start_index:
                end_index -= 1
            if arr[end_index] != 0:
                arr[start_index] = arr[end_index]
                start_index +=1
                end_index -= 1




"""interpretations of a number string?
a=1,b=2,z=26 etc

11 = 2 (aa, k)
111 = 3 (aaa, ak, ka)
90 = 0
20 = 1 (t)
"""
def numberOfInterpretations(numberString):
    counts = [None for _ in numberString]
    return interpretation_count(numberString,counts)
def interpretation_count(numberString,counts):
    if  numberString == '0' or numberString == '':
        return 0
    digit = int(numberString[0])
    if digit == 0:
        return 0
    num = int(numberString)
    if  num < 11 or num == 20:
        return 1
    if num < 27:
        return 2
    index = len(numberString) - 1
    if counts[index] == None:
        count =  numberOfInterpretations(numberString[1:])
        digits = int(numberString[0:2])
        if digits < 27:
            count += numberOfInterpretations(numberString[2:])
        counts[index] = count
    return counts[index]

if __name__ == "__main__":
    arr = [1, 0, 3, 1, 2, 0, 5, 0]
    removeZeros(arr)
    print arr
    print numberOfInterpretations('11')
    print numberOfInterpretations('111')
    print numberOfInterpretations('90')
    print numberOfInterpretations('20')
    print numberOfInterpretations('1119')
    print numberOfInterpretations('00')
    print numberOfInterpretations('200')
    print numberOfInterpretations('202')
