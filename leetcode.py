def length_of_longest_substring(s):
    """
    :type s: str
    :rtype: int- length of longest substring with unique characters
    """

    string_length = len(s)
    if string_length < 2:
        return string_length
    length = 0
    front = 0
    characters = set(s[front])
    back = 1
    while True:
        while back < string_length and s[back] not in characters:
            characters.add(s[back])
            back += 1
        #repeated character found
        diff = back - front
        if diff > length:
            length = diff  #store length of longest found so far
        if back == string_length:
            return length
        #remove characters until repeat found
        while s[front] != s[back]:
            characters.remove(s[front])
            front += 1
        #remove repeated character
        characters.remove(s[front])
        front += 1

def median_of_sorted_arrays(nums1,nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    if len1 == 0:
        if len2 == 0:
            return None
        middle = len2/2
        if len2%2 == 1:
            return nums2[middle]*1.0
        else:
            return (nums2[middle] + nums2[middle - 1])/2.0
    if len2 == 0:
        middle = len1/2
        if len1%2 == 1:
            return nums1[middle]*1.0
        else:
            return (nums1[middle] + nums1[middle - 1])/2.0
    length = len1 + len2
    index1 = 0
    index2 = 0
    count = 0
    middle = length/2
    median = 0
    while count <= middle:
        if nums1[index1] < nums2[index2]:
            previous = median
            median = nums1[index1]
            index1 += 1
        else:
            previous = median
            median = nums2[index2]
            index2 += 1
        count += 1
        if index1 == len1:
            median_index = index2 - count + middle
            median = nums2[median_index]
            if median_index == 0:
                previous = nums1[-1]
            else:
                previous = nums2[median_index - 1]
            break
        elif index2 == len2:
            median_index = index1 - count + middle
            median = nums1[median_index]
            if median_index == 0:
                previous = nums2[-1]
            else:
                previous = nums1[median_index - 1]
            break
    #determine if median is average of two or simply middle value
    if length%2 == 1:
        return median*1.0
    else:
        return (median + previous)/2.0

def max_palindromic_substring(input_string):
    """
    Input: string
    Output: string representing the longest palindromic substring of the input string
    """
    length = len(input_string)
    if length < 2:
        return input_string
    palindrome_length = 1
    index= (0,0)
    grid = [[0 for _ in range(length + 1)] for _ in range(length + 1)]
    backwards_string = input_string[::-1]
    for i in range(1,length + 1):
        for j in range(1,length + 1):
            if input_string[j-1] == backwards_string[i-1]:

                run_length = 1 + grid[i-1][j-1]
                grid[i][j] = run_length
                #if actual palindrome & longest yet, store it
                if (run_length > palindrome_length) & ((length-j)==(i-run_length)):  #track longest
                    palindrome_length = run_length
                    index = (i ,j)
            else:
                grid[i][j] = 0

    i = index[0]
    j = index[1]
    if index == (0,0):
        return input_string[0]
    #walk back to start of palindrome
    while grid[i][j] > 0:
        i -= 1
        j -= 1
    return input_string[j:j+palindrome_length]

def zig_zag_conversion(input_string,number_of_rows):
    """
    input_string: strings
    number_of_rows: integer
    output: string reordered in zig-zag pattern using given number of rows
    """
    length = len(input_string)
    if number_of_rows < 1:
        return ""
    if length < number_of_rows or number_of_rows < 2:
        return input_string
    lists = [[] for _ in range(number_of_rows)]
    count = 0
    delta = 1
    index = 0
    while count < length:
        lists[index].append(input_string[count])
        count += 1
        index += delta
        if index == 0 or index == number_of_rows-1:  #time to reverse direction
            delta = delta * (-1)
    zig = lists[0]
    for i in range(1,number_of_rows):
        zig.extend(lists[i])
    return "".join(zig)
def is_palindrome_number(number):
    if number <0:
        return False
    n = 0
    while number/pow(10,n) > 0:
        n += 1
    n -= 1 #greatest power of ten in number
    while n > 0:
        most_significant_digit = number/pow(10,n)
        least_significant_digit = number%10
        if most_significant_digit != least_significant_digit:
            return False
        number = (number%pow(10,n))/10
        n -=2
    return True

def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
if __name__ == '__main__':
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("abcdef") == 6
    assert length_of_longest_substring("abbb") == 2
    assert length_of_longest_substring("abcabcde") == 5
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("anviaj") == 5
    nums1 = [1]
    nums2 = [2,5,6,8]
    assert  median_of_sorted_arrays(nums1,nums2) == 5
    nums1.extend([3,4,9])
    assert  median_of_sorted_arrays(nums1,nums2) == 4.5
    nums1 = []
    assert  median_of_sorted_arrays(nums1,nums2) == 5.5
    nums2 = []
    assert  median_of_sorted_arrays(nums1,nums2) == None
    nums1 = [2,4,5,8]
    assert  median_of_sorted_arrays(nums1,nums2) == 4.5
    nums2 = [1,5,6,7]
    assert  median_of_sorted_arrays(nums1,nums2) == 5.0
    nums1 = [1]
    nums2 = [2,3]
    assert  median_of_sorted_arrays(nums1,nums2) == 2.0

    assert max_palindromic_substring("pal") == "p"
    assert max_palindromic_substring("pallap") == "pallap"
    assert max_palindromic_substring("vvbpap") == "pap"
    temp = max_palindromic_substring("papa")
    assert temp == "apa" or temp == "pap"
    assert max_palindromic_substring("palap") == "palap"
    assert max_palindromic_substring("vbpap") == "pap"
    assert max_palindromic_substring("ppl") == "pp"
    assert max_palindromic_substring("") == ""

    temp = max_palindromic_substring("babad")
    assert temp == "aba" or temp == "bab"
    assert max_palindromic_substring("cbbd") == "bb"
    print max_palindromic_substring("abcdecba")
    assert zig_zag_conversion("PAYPALISHIRING",3) ==  "PAHNAPLSIIGYIR"
    assert zig_zag_conversion("",3) == ""
    assert zig_zag_conversion("HELLOWORLD",0) == ""
    assert zig_zag_conversion("HELLOWORLD",1) == "HELLOWORLD"
    assert zig_zag_conversion("ABCD",2) == "ACBD"
    assert zig_zag_conversion("HELP",3) == "HEPL"
    assert zig_zag_conversion("HELLOWORLD",4) == "HOEWRLOLLD"
    assert is_palindrome_number(0) == True
    assert is_palindrome_number(101) == True
    assert is_palindrome_number(1001) == True
    assert is_palindrome_number(-10) == False
    assert is_palindrome_number(10) == False
    assert is_palindrome_number(5) == True
    assert is_palindrome_number(55) == True
    assert is_palindrome_number(565) == True
    assert is_palindrome_number(5665) == True
    assert is_palindrome_number(123) == False




    print "all tests passed"
