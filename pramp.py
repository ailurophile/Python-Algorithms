from collections import defaultdict
from collections import Counter

def word_count_engine(document):
    """Document scanning function wordCountEngine,
     Input: document string
     Output: list of tuples of lower-cased words with punctuation removed and their frequencies
     in descending order."""

    words = document.split(' ')
    words_only = []
    for word in words:
        words_only.append(''.join([i for i in word.lower() if i.isalpha()]))
        word_count= defaultdict(int)
    for word in words_only:
        word_count[word] += 1
    pairs = word_count.items()
    sorted_pairs = counting_sort(pairs)
    return sorted_pairs

def find_max(tuples):
    max =0
    for word, count in tuples:
        if count > max:
          max = count
    return max
def counting_sort(tuples):
    max = find_max(tuples)
    #create array to hold frequencies
    counts = [0 for _ in range(max+1)]
    for word, count in tuples:
        counts[count] += 1  #counts array now holds number of words of frequency index
    sum = 0
    for i in range(len(counts)):
        sum += counts[i]
        counts[i] = sum  #counts array now holds number of word frequencies equal to or smaller than index
#dimension output array
    output = [("dummy",0) for _ in range(len(tuples)+1)]
    for tuple in tuples:

        output[counts[tuple[1]]] = tuple
        counts[tuple[1]] -= 1
    return output[-1:1:-1]
#    return output[1:]
def word_counter_engine(document):
    """Document scanning function wordCountEngine using Counter object
    Input: document string
    Output: list of tuples of lower-cased words with punctuation removed and their frequencies
    in descending order."""
    words = document.split(' ')
    words_only = []
    for word in words:
        words_only.append(''.join([i for i in word.lower() if i.isalpha()]))
    word_count = Counter(words_only)
    return word_count.most_common()

def spiral_copy(inputMatrix):
    """Input: a 2D array inputMatrix of integers
    Output: 1D array of integers from inputMatrix in a spiral order, clockwise."""

    if inputMatrix == None:
        return []
    row_stop = len(inputMatrix)  #final position to process in current row
    column_stop = len(inputMatrix[0]) #final position to process in current column
    steps =  row_stop * column_stop
    output = []
    row_index = 0
    column_index = 0
    spiral = 0  #to use as bumper on right and up iterations
    while steps > 0:
        while column_index < column_stop and steps > 0:
             output.append(inputMatrix[row_index][column_index])
             column_index += 1
             steps -= 1
        column_index -= 1
        column_stop -= 1
        while row_index < row_stop -1 and steps > 0:  # -1 because we must advance first
            row_index += 1
            output.append(inputMatrix[row_index][column_index])
            steps -= 1
        row_stop -= 1
        while column_index > spiral and steps > 0:
            column_index -= 1
            output.append(inputMatrix[row_index][column_index])
            steps-=1
        spiral += 1
        while row_index > spiral and steps > 0:
            row_index-=1
            output.append(inputMatrix[row_index][column_index])
            steps-=1
        column_index += 1
    return output
if __name__ == '__main__':
    inputMatrix  = [ [1,    2,   3,  4,    5],
                    [6,    7,   8,  9,   10],
                    [11,  12,  13,  14,  15],
                    [16,  17,  18,  19,  20] ]
    for input_row in inputMatrix:
        print input_row
    print spiral_copy(inputMatrix)
    matrix2 = [[i*j for i in range (1,11)] for j in range(1,11)]

    for matrix_row in matrix2:
        print matrix_row
    print spiral_copy(matrix2)
    matrix3 = [[1,2,3,4,5],[10,9,8,7,6]]
    for matrix_row in matrix3:
        print matrix_row
    print spiral_copy(matrix3)
    matrix4 = [[0,1,2],[9,10,3],[8,11,4],[7,6,5]]
    for matrix_row in matrix4:
        print matrix_row
    print spiral_copy(matrix4)
    matrix5 = [[1],[2],[3]]
    print spiral_copy(matrix5)

    document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
    print word_count_engine(document)
    print word_counter_engine(document)
