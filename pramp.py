from collections import defaultdict
from collections import Counter
from collections import deque

def reverse_words(arr):
    result = deque()
    word = []
    for char in arr:
        if char != ' ':
            word.append(char)
        else:
            result.appendleft(word)
            word = []
    #get final word which had no space delimiter
    result.appendleft(word)
    results = []
    for each in result:
        results.extend(each)
        results.append(' ')
    results.pop()  #no space needed at end
    return results

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
"""
Input: n: Positive integer, x: nonnegative number
Output: nth root of input using no library functions
"""
def root(x, n):
    def absolute_value(x):
        if x < 0:
            x = x*(-1)
        return x
    def power(x,n):
        y = x
        for _ in range(n-1):
            y = y * x
        return y
    if x == 0:
         return 0
    max_guess = x
    min_guess = 0.0
    if x < 1:
        max_guess = 1
    current_guess = (min_guess + max_guess)/2.0
    current_delta = x - power(current_guess,n)
    while absolute_value(current_delta) >= .001:
        if current_delta < 0:
      # go smaller!!!!!
            max_guess = current_guess
        else:
            min_guess = current_guess
        current_guess = (min_guess + max_guess)/2
        current_delta = x - power(current_guess,n)
    return current_guess
"""
Input: starting Node
Output: integer minimum sales cost to dealer (leaf)
The car manufacturer Honda holds their distribution system
in the form of a tree (not necessarily binary). The root is
the company itself, and every node in the tree represents a
car distributor that receives cars from the parent node and
ships them to its children nodes. The leaf nodes are car
dealerships that sell cars direct to consumers. In addition,
every node holds an integer that is the cost of shipping a
car to it.Honda wishes to find the minimal Sales Path cost
in its distribution tree. Given a node rootNode, write an
function getCheapestCost that calculates the minimal Sales
Path cost in the tree. Range(rootNode.cost) =  (0,100000)
"""
def get_cheapest_cost(rootNode):
    if rootNode.children ==  []:
       return rootNode.cost
    cost = 1000000
    for child in rootNode.children:
       new_cost = get_cheapest_cost(child)
       if new_cost < cost:
                cost = new_cost
    return cost + rootNode.cost

class Node:

  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
"""
Definition as above for get_cheapest_cost, alter the function in
order to return all Sales Paths with the minimal cost in an array.
"""
def routes_helper(rootNode,routes):
    if rootNode.children ==  []:
        return rootNode.cost,[[rootNode.cost]]
    cost = 1000000
    for child in rootNode.children:
        new_cost, new_routes = routes_helper(child, [[child.cost] +routes[0]])
        if new_cost < cost:
            cost = new_cost
            results = [[rootNode.cost] + route for route in new_routes]
        elif new_cost == cost:
            results.extend([[rootNode.cost] + route for route in new_routes] )
    return cost + rootNode.cost, results

def get_cheapest_routes(rootNode):
    return routes_helper(rootNode,[[]])
def shortest_substring(input_string,characters):
    """
    Given an array of unique characters and a string, Implement a function that finds
    the smallest substring of the string containing all the characters. Return
    empty string if such a substring does not exist.


    [time limit] 5000ms

    Range of character array length = [1,30]
    Range of input string length = [1,500]

    """
    character_counts = Counter(characters)
    string_counts = Counter()
    matches = 0
    target_matches = len(characters)
    start = 0
    string_length = len(input_string)
    if target_matches == 0 or string_length == 0:
        return ""
    for char in input_string:
        if char in characters:
            string_counts[char] += 1
    for char in characters:
        if char not in string_counts or character_counts[char] > string_counts[char]:
            return ""  #No substring possible
    extras = sum(string_counts.values()) - sum(character_counts.values())
    string_counts.clear()
    while input_string[start] not in character_counts:
        start += 1  #advance to first occurence of a target character
    #add character to Counter and increment match count
    string_counts[input_string[start]] += 1
    matches += 1
    end =  start + 1
    while matches < target_matches:
        if input_string[end] in character_counts:
            string_counts[input_string[end]] += 1
            if string_counts[input_string[end]] <=  character_counts[input_string[end]]:
                matches += 1
            else:
                 extras -= 1  #breaks zyx
        end += 1
    substring_length = end - start
    substring_start = start
    if substring_length == target_matches:
        return input_string[start:end]

    while end < string_length and extras > 0 :
        if input_string[end] in character_counts:
            string_counts[input_string[end]] += 1
            if string_counts[input_string[end]] >  character_counts[input_string[end]]:
                extras -= 1
            end += 1
        else:
            end += 1
            continue
        #drop unnecessary characters off of front
        while True:
            while  input_string[start] not in character_counts:
                start += 1
            while string_counts[input_string[start]] > character_counts[input_string[start]]:
                string_counts[input_string[start]] -= 1
                start += 1
            if input_string[start] in character_counts and string_counts[input_string[start]] <= string_counts[input_string[start]]:
                break
        if end - start < substring_length:
            substring_length = end - start
            substring_start = start
    return input_string[substring_start:substring_start+substring_length]

def array_of_array_products(arr):
    """
    Input: array of integers, arr
    Output:  array of products where products[i] contains the product of all integers in
    the input array except arr[i]

    """
    product = 1
    product_array = []
    if len(arr) < 2:
        return product_array
    for i in range(len(arr)):
        for each in arr[0:i]+arr[i+1:]:
            product = product*each
        product_array.append(product)
        product = 1
    return product_array
def find_duplicates(arr1, arr2):
    """
    Input: two arrays sorted in ascending order
    Output: Array of items found in both input arrays in sorted order

    """
    len1 = len(arr1)
    len2 = len(arr2)
    if len1 > 10*len2 or len2 > 10*len1:
        return disparate_find_duplicates(arr1,arr2)
    index1 = 0
    index2 = 0
    results = []
    while index1 < len1 and index2 < len2:
        if arr1[index1] < arr2[index2]:
            index1+= 1
        elif arr1[index1] == arr2[index2]:
          results.append(arr1[index1])
          index1 += 1
          index2 += 1
        else:
          index2 += 1
    return results
def disparate_find_duplicates(arr1, arr2):
    """
    Input: two arrays sorted in ascending order
    Output: Array of items found in both input arrays in sorted order
    To be used when one array is much longer than the other

    """
    def binary_search(value,array,start,end):
        middle = (end + start)/2
        if end - start < 2 :
            return value == array[end-1] | value == array[start]
        if value == array[middle]:
            return True
        if value > array[middle]:
            return binary_search(value,array,middle+1,end)
        else:
            return binary_search(value,array,start,middle)

    len1 = len(arr1)
    len2 = len(arr2)
    if len1 > len2:
        short_length = len2
        short_array = arr2
        long_length = len1
        long_array = arr1
    else:
        short_length = len1
        short_array = arr1
        long_length = len2
        long_array = arr2
    results = []
    for each in short_array:
        if binary_search(each,long_array,0,long_length):
            results.append(each)
    return results
def find_pairs_with_given_difference(arr, k):
  """
  input: array of integers, target difference
  output: array of ordered pairs where the x and y values are both in the input array
  and where x - y = k

  """
  if k < 0 or arr == []:
    return []
  output = []
  hash = {}
  for value in arr:
    if value not in hash:
      hash[value] = 1
  for value in arr:
    diff = value - k
    if diff in hash:
      output.append((value,diff))
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
    print root(7,3)
    print root(9,2)
    print root(.25,2)
    arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ',
                'm', 'a', 'k', 'e', 's', ' ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
    print reverse_words(arr)
    arr2 = ["a"," "," ","b"]
    print reverse_words(arr2)
    print reverse_words([" "," "])
    node1 = Node(0)
    node2 = Node(5)
    node3 = Node(3)
    node4 = Node(4)
    node1.children = [node2,node3]
    node2.children = [node4]

    print get_cheapest_cost(node1)
    print get_cheapest_routes(node1)

    node5 = Node(2)
    node6 = Node(0)
    node7 = Node(1)
    node8 = Node(10)
    node9 = Node(1)
    node3.children = [node5,node6]
    node5.children = [node7]
    node7.children = [node9]
    node6.children = [node8]
    print get_cheapest_cost(node1)
    print get_cheapest_routes(node1)
    node10 = Node(6)
    node11 = Node(1)
    node12 = Node(5)
    node1.children.append(node10)
    node10.children = [node11,node12]
    print get_cheapest_cost(node1)
    print get_cheapest_routes(node1)
    print shortest_substring("I'm an ailurophile. I love cats",['c','a','t','s','a'])
    print shortest_substring("I'm an ailurophile. I love cats",['a','a'])
    print shortest_substring("I'm an ailurophile. I love cats",['d','a','t','s','a'])
    print shortest_substring("ADOBECODEBANCDDD",['A','B','C'])
    print shortest_substring("ADOBECODEBANCDDD",[])
    print shortest_substring("xyyzyzyx",['x','y','z'])
    print shortest_substring("",['A','B','C'])
    arr = [8, 10, 2]
    print array_of_array_products(arr)
    arr = [0]
    print array_of_array_products(arr)
    print array_of_array_products([1,2,3,4,5])
    arr1 = [1,3,5,9]
    arr2 = [2,3,4,6,9,10]
    print(find_duplicates(arr1, arr2))
    print(disparate_find_duplicates(arr1, arr2))
    print find_pairs_with_given_difference([0, -1, -2, 2, 1],1)
    print find_pairs_with_given_difference([0, -1, -2, 2, 1],2)
    print find_pairs_with_given_difference([1, 7, 5, 3, 32, 17, 12],17)
