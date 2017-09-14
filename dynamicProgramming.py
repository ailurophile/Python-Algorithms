import time
import math
import random

def time_execution(code):
   start = time.clock()  # start the clock
   result = eval(code)  # evaluate any string as if it is a Python command
   run_time = time.clock() - start  # find difference in start and end time
   return result, run_time  # return the result of the code and time taken

def number_of_paths(n):
    """Returns the number of paths to the top of a flight of n stairs taking
    1, 2 or 3 stairs at each step"""
    if n  < 1:
        return 0
    counts = [-1 for _ in range(n+1)]
    counts[1] = 1
    counts[2] = 2  #1-1; 2
    counts[3] = 4   #1-2; 2-1; 1-1-1; 3

    count_paths(n, counts)
    return counts[n]

def count_paths(stairs, count):
    if count[stairs] == -1:
        count[stairs]= count_paths(stairs - 1, count) + count_paths(stairs - 2, count)+ count_paths(stairs - 3, count)
    return count[stairs]

def count_coins_to_value(value):
    """Return number of ways to create value using quarters, dimes, nickels, and pennies"""
    if value < 1:
        return 0
    coins = [25,10,5,1]
    counts = [0 for _ in range(value + 1)]  #for memoization
    count_coins(value,coins, counts)
    return counts[value]

def count_coins(value,coins, counts):
    if counts[value] != 0:
        return counts[value]
    coin = coins[0]
    if coin == 1:
        return 1  #only one way to make value using pennies
    count = 0
    for i in range(value/coin + 1):  #count ways with 0 - max possible of coin
        count += count_coins(value - i*coin, coins[1:], counts)
    counts[value] = count
    return count

def queen_placements():
    """Returns the number of ways to safely position 8 queens on an 8x8 chess board"""
    results = []
    for col in range(8):
        place_queens([], 0, col,results)

    return results


def place_queens( queens_array, row, column, paths):
    results = []

    if is_path_clear(queens_array, row, column):
    #place queen on grid
        new_placement = queens_array + [(row,column)]
        if row == 7:
            paths.append(new_placement)#valid placement of 8 found
            return
        #get placement for next row
        for col in range(8):
            place_queens(new_placement, row + 1, col, paths)



def is_path_clear(array, row, column):
    """returns false if an entry is array shares a row, column or diagonal with (row,column)
    else returns True"""
    for spot in array:
        if spot[0] == row or spot[1] == column:
            return False
        if abs(spot[0] - row) == abs(spot[1] - column):
            return False
    return True
def max_ones_submatrix(matrix):
    """
    Input: binary matrix
    Output: Integer representing the largest submatrix containing all ones
    """
    number_of_rows = len(matrix)
    if number_of_rows == 0:
        return 0
    number_of_columns = len(matrix[0])
    if number_of_columns == 0:
        return 0
    max_size = 0

    sums_matrix = [[0 for _ in range(number_of_columns)] for _ in range(number_of_rows)]
    for i in range(number_of_columns):
        if matrix[0][i] == 1:
            sums_matrix[0][i] = 1
            max_size = 1
    for j in range(number_of_rows):
        if matrix[j][0] == 1:
            sums_matrix[j][0]= 1
            max_size = 1
    for row in range(1,number_of_rows):
        for col in range(1,number_of_columns):
            if matrix[row][col] == 1:
                sum = 1 + min(sums_matrix[row-1][col],sums_matrix[row][col-1],sums_matrix[row-1][col-1])
                if sum > max_size:
                    max_size = sum
                sums_matrix[row][col] = sum
    return max_size

def longest_common_substring(s1,s2):
    """
    Input: 2 strings
    Output: Integer representing the length of the longest substring of both input strings
    """
    max_substring = 0
    # check for special cases
    if s1 == "" or s2 == "":
        return 0
    l1 = len(s1)
    l2 = len(s2)
    if l1 == 1:
        if s1[0] in s2:
            return 1
        return 0
    if l2 == 1:
        if s2[0] in s1:
            return 1
        return 0
    # build table of zeroes one row and one column longer than lengths of s1 & s2
    counts_table = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]
    for i in range(1,l2+1):  #rows based on length of s2
        for j in range(1,l1+1):  # columns based on length of s1
            if s1[j-1] == s2[i-1]:  #indices for table off by 1 because extra zero row & column
                new_length = 1 + counts_table[i-1][j-1]
                counts_table[i][j] = new_length  #extend length of substring (on diagonal)
                if new_length > max_substring:  #if longest yet, save it
                    max_substring = new_length
    return max_substring
def max_rod_price(rod_length,prices):
    """
    Inputs: integer rod length, array of prices per unit where unit = index
    Output: maximum value obtainable from rod
    Naive top down recursive approach
    """
    if rod_length < 1 or prices == []:
        return 0
    longest = len(prices)
    pieces = rod_length/longest
    max_price = 0
    for i in range(pieces + 1):
        price =i* prices[longest-1] + max_rod_price(rod_length - i*longest, prices[:-1])
        if price > max_price:
            max_price = price
    return max_price

def max_rod_value(rod_length,prices):
    """
    Inputs: integer rod length, array of prices per unit where unit = index
    Output: maximum value obtainable from rod
    Bottom up dynamic programming approach
    """
    if rod_length < 1 or prices == []:
        return 0
    pieces = len(prices)
    values = [0 for _ in range(max(rod_length,pieces) + 1)]
    # copy prices into values array
    for i in range(pieces):
        values[i+1] = prices[i]
    #find best price for each progressively longer piece using previously saved values
    for i in range(1,rod_length+1):
        max_value = values[i]
        for j in range((i+1)/2):
            value = values[j+1] + values[i-1-j]
            if value > max_value:
                max_value = value
        values[i] = max_value
    return values[rod_length]
def max_palindromic_substring(input_string):
    """
    Input: string
    Output: string representing longest palindromic substring of input string
    """
    length = len(input_string)
    grid = [[False for _ in range(length)] for _ in range(length)]
    longest = 1
    index = (0,0)
    #base case palindromes
    for i in range(length):
        grid[i][i] = True
        if (i < length-1) and (input_string[i] == input_string[i+1]):
            grid[i][i+1] = True
            longest = 2
            index = (i,i+1)
    for i in range(length - 1,-1,-1):
        for j in range(i+2,length):
            if grid[i][j]  == False:  #don't overwrite base case pairs
                is_palindrome = grid[i+1][j-1] & (input_string[i] == input_string[j])
                if is_palindrome:
                    palindrome_length = j - i + 1
                    grid[i][j] = True
                    if palindrome_length > longest:
                        longest = palindrome_length
                        index = (i,j)
    return input_string[index[0]:index[1]+1]











if __name__ == '__main__':
    """
    placements = queen_placements()
    print "placement count = %d" % len(placements)
    print placements
    print("testing coins")
    print count_coins_to_value(12)
    print count_coins_to_value(10)
    print count_coins_to_value(1)
    print count_coins_to_value(5)
    print count_coins_to_value(32)
    matrix = [
    [1,1,1,1],
    [1,0,1,1],
    [1,1,1,1],
    [1,0,1,1],
    [0,1,1,1]]
    print max_ones_submatrix(matrix)
    matrix = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]]
    print max_ones_submatrix(matrix)
    m = [[]]
    print max_ones_submatrix(m)
    m = [[1]]
    print max_ones_submatrix(m)
    m = [[0]]
    print max_ones_submatrix(m)
    print "testing substrings"
    s2 = "i"
    s1 = "isnt"
    print longest_common_substring(s1,s2)
    s2 = ""
    print longest_common_substring(s1,s2)
    s2 = "wasnt"
    print longest_common_substring(s1,s2)
    s2 = "isasasntt"
    print longest_common_substring(s1,s2)
    s2 = "asasnt"
    print longest_common_substring(s1,s2)
    s1 = "tissuesasa"
    print longest_common_substring(s1,s2)
    s2 = "su"
    print longest_common_substring(s1,s2)
    """
    prices = [1,5,8,9,10,17,17,20]
    print max_rod_price(8,prices)
    print max_rod_value(8,prices)
#    print time_execution('max_rod_price(80,prices)')
#    print time_execution('max_rod_value(80,prices)')
    prices = [3,5,8,9,10,17,17,20]
    print max_rod_price(9,prices)
    print max_rod_value(9,prices)
    prices = [1,5,5,5,6,7,17,20]
    print max_rod_price(6,prices)
    print max_rod_value(6,prices)
    prices = [0,6,1,2,6,7,7,8]
    print max_rod_price(9,prices)
    print max_rod_value(9,prices)
    assert max_palindromic_substring("abac") == "aba"
    assert max_palindromic_substring("pal") == "p"
    assert max_palindromic_substring("pallap") == "pallap"
    assert max_palindromic_substring("vvbpap") == "pap"
    temp = max_palindromic_substring("papa")
    assert temp == "apa" or temp == "pap"
    assert max_palindromic_substring("palap") == "palap"
    assert max_palindromic_substring("vbpap") == "pap"
    assert max_palindromic_substring("ppl") == "pp"
    assert max_palindromic_substring("") == ""
    assert max_palindromic_substring("a") == "a"
    assert max_palindromic_substring("aa") == "aa"
    assert max_palindromic_substring("aaa") == "aaa"
    assert max_palindromic_substring("aaaa") == "aaaa"
    assert max_palindromic_substring("aabaa") == "aabaa"
    assert max_palindromic_substring("baabbaa") == "aabbaa"
    temp = max_palindromic_substring("babad")
    assert temp == "aba" or temp == "bab"
    assert max_palindromic_substring("cbbd") == "bb"
    assert max_palindromic_substring("abcdecba") == "a"
