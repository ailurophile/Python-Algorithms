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
    return output[-1:0:-1]
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
def rotate(matrix, clockwise = True):
    n = len(matrix[0])
    m = len(matrix)
    if clockwise == True:
        rotated = [[matrix[row][col] for row in range(m-1,-1,-1)] for col in range(n)]
    else:
        rotated = [[matrix[row][col] for row in range(m)] for col in range(n-1,-1,-1)]



    return rotated

"""
You are testing a new driverless car that is located at the southwest corner of an
nxn grid.  The car is supposed to get to the opposite corner without dipping into
the top half of the grid so x>=y always.  Given n, the size of one axis of the grid,
write a function that returns the number of possible paths the car can take.  In each
step the car may move one position north or 1 position east.

Input: n range [1,100]
Output integer count of paths

"""


def num_of_paths_to_dest(n):
    """
    returns number of paths for driverless car to reach upper right corner of nxn grid from
    lower left not using memoization staying entirely within the lower half of the grid y<x
    moving one position north or east at each step.
    """
    if n < 1:
        return 0
    position = (0,0)
    return step(position, n)

def step(position, end):
    if position[0] == end and position[1] == end:
        return 1
    if position[0] < position[1]:
        return 0
    if position[0] > end or position[1] > end:
        return 0
    x = position[0] + 1
    y = position[1] + 1
    return step((x,position[1]), end) + step((position[0],y),end)

def number_of_paths_to_dest(n):
    """
    returns number of paths for driverless car to reach upper right corner of nxn grid from
    lower left using memoization staying entirely within the lower half of the grid y<x
    moving one position north or east at each step.
    """
    def num_paths(x,y,paths):
        if x < 0 or y < 0:
            return 0
        if y > x:
            paths[x][y] = 0
            return 0
        if paths[x][y] == -1:
            paths[x][y] = num_paths(x-1,y,paths) + num_paths(x,y-1,paths)
        return paths[x][y]
    if n < 1:
        return 0
    memo = [[-1 for i in range(n+1) ] for j in range(n+1)]
    memo[0][0] = 1  #base case
    for j in range(n+1):
        for i in range(j):
            memo[i][j]=0
    return num_paths(n,n,memo)

def deletion_distance(str1, str2):
    """
    Returns the minimum number of characters you need to delete from the two
    input strings in order to get the same string.

    """
    memo = [[-1 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

    return deletion_helper(str1,str2,memo)
    
def deletion_helper(str1,str2,distances):
    if str1 == "":
        return len(str2)
    if str2 == "":
        return len(str1)

    if distances[len(str1)][len(str2)] == -1:
        if str1[-1] == str2[-1]:
            distances[len(str1)][len(str2)] = deletion_helper(str1[:-1],str2[0:-1],distances)
        else:
            distances[len(str1)][len(str2)] = 1 + min(deletion_helper(str1,str2[:-1], distances),
            deletion_helper(str1[:-1], str2,distances))
    return distances[len(str1)][len(str2)]

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
    rotated = rotate(matrix2)
    for each in matrix2:
        print each
    for each in rotated:
        print each
    rotated = rotate(matrix2, False)
    for each in rotated:
        print each
    rotated = rotate(matrix4)
    for each in matrix4:
        print each
    for each in rotated:
        print each
    rotated = rotate(matrix4,False)
    for each in rotated:
        print each


    document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
    print word_count_engine(document)
    print word_counter_engine(document)
    for n in range(6):
        print number_of_paths_to_dest(n)
    print number_of_paths_to_dest(100)
    print deletion_distance("hit","heat")
    print deletion_distance("","heat")
    print deletion_distance("heharit","hearth")
    print deletion_distance("%","heat")
    print deletion_distance("","")
