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

def max_volume(heights):
    """
    Input: array of numbers
    Output: maximum volume of water container can hold using numbers in array
    as heights and positions as distances apart assuming a depth of 1 unit.
    """
    def volume(index1,index2):
        tall = max(heights[index1],heights[index2])
        short = min(heights[index1],heights[index2])
        return (index2 - index1)*short
    front = 0
    back = len(heights) - 1
    current_volume = volume(front,back)
    front_height = heights[front]
    back_height = heights[back]
    while front < back:
        if front_height>back_height:
            #try to make back taller
            back -= 1
            if (heights[back] > back_height):
                vol = volume(front,back)
                if vol > current_volume:
                    current_volume = vol
                back_height = heights[back]
        else:
            #try to make front taller
            front += 1
            if (heights[front] > front_height):
                vol = volume(front,back)
                if vol > current_volume:
                    current_volume = vol
                front_height = heights[front]
    return current_volume

def integer_to_roman(target):
    """
    Input: integer
    Output: string representing input integer in Roman numerals
    """
    output = []
    ones = [[],['I'],['I','I'],['I','I','I'],['I','V'],['V'],['V','I'],
    ['V','I','I'],['V','I','I','I'],['I','X']]
    while target >= 1000:
        output.append('M') #1000
        target -= 1000
    if target >= 900:
        output.extend(['C','M']) #900
        target -= 900
    if target >= 500:
        output.append('D') #500
        target -= 500
    if target >= 400:
        output.extend(['C','D']) #400
        target -= 400
    while target >= 100:
        output.append('C') #100
        target -= 100
    if target >= 90:
        output.extend(['X','C']) #90
        target -= 90
    if target >= 50:
        output.append('L') #50
        target -= 50
    if target >= 40:
        output.extend(['X','L']) #40
        target -= 40
    while target >= 10:
        output.append('X') #10
        target -= 10
    output.extend(ones[target])
    return ''.join(output)
def longest_common_prefix(strings):
    number_of_strings = len(strings)
    if number_of_strings == 0:
        return ""
    shortest_index = 0
    shortest = len(strings[0])
    if shortest == 0:
        return ""
    index = 0
    prefix = []
    current_character = strings[0][0]
    #find shortest string
    for i,s in enumerate(strings):
        length = len(s)
        if length == 0:
            return ""
        if length < shortest:
            shortest = length
            shortest_index = i
        if s[index] != current_character:
            return "".join(prefix)
    word = strings.pop(shortest_index)
    prefix.append(current_character)
    for i in range(1,shortest):
        current_character = word[i]
        for s in strings:
            if s[i] != current_character:
                return "".join(prefix)
        prefix.append(current_character)
    return "".join(prefix)



def letter_combinations(digits):
    """
    Input: String of digits
    Output: All possible letter combination strings represented by the numbers
     using mappings from telephone keys
    """
    digits = "".join([i for i in digits if (i != '1' and i!='0')])
    if digits == "":
        return []
    letter_map = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
    '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
    '8': ['t','u','v'], '9': ['w','x','y','z']}
    array = [[]]
    for digit in digits:
        array = [each + [letter] for letter in letter_map[digit]for each in array]
    return [''.join(combo) for combo in array]
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def append(self,node):
        if self.next == None:
            self.next = node
        else:
            n = self.next
            while n.next:
                n = n.next
            n.next = node
    def __repr__(self):
        output = [self.val]
        n = self.next
        while n:
            output.append(n.val)
            n = n.next
        return str(output)
def merge_k_lists(lists):

    def merge_lists(l1,l2):
        if l1 == []:
            return l2
        if l2 == []:
            return l1
        if l1.val < l2.val:
            output_list = l1
            previous = l1
            next_node = l1.next
            to_insert = l2
        else:
            output_list = l2
            previous = l2
            next_node = l2.next
            to_insert = l1
        while to_insert != None:
            while next_node != None and to_insert.val > next_node.val:
                previous = next_node
                next_node = next_node.next
            if next_node == None:
                previous.next = to_insert #append remainder of other list to end
            else:
                previous.next = to_insert
                temp = to_insert.next
                to_insert.next = next_node
                to_insert = temp
                previous = previous.next
        return output_list


    while len(lists) > 1:
        lists.append(merge_lists(lists.pop(0),lists.pop(0)))
    return lists[0]


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
    assert  median_of_sorted_arrays(nums2,nums1) == 2.0

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
    assert max_palindromic_substring("abcdecba") == "a"
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
    assert max_volume([1,2,1,4]) == 4
    assert max_volume([1,4,1,2]) == 4
    assert max_volume([1,4,1,4]) == 8
    assert max_volume([1,2,1,5,1,1,1,1,3]) == 15
    assert max_volume([1,2,1,5,1,1,1,4,3]) == 16
    assert max_volume([0,2]) == 0
    assert max_volume([1,2,4,3]) == 4
    assert max_volume([2,3,4,5,18,17,6]) == 17
    assert integer_to_roman(50) == "L"
    assert integer_to_roman(55) == "LV"
    assert integer_to_roman(0) == ""
    assert integer_to_roman(490) == "CDXC"
    assert integer_to_roman(4149) == "MMMMCXLIX"
    assert integer_to_roman(10) == "X"
    assert longest_common_prefix(["hello","hollo"]) == "h"
    assert longest_common_prefix(["hello","world"]) == ""
    assert longest_common_prefix(["hello","help","helter"]) == "hel"
    assert longest_common_prefix(["hello","world",""]) == ""
    assert longest_common_prefix([]) == ""
    print letter_combinations("2")
    print letter_combinations("23")
    print letter_combinations("1204")
    print letter_combinations("1354")
    print letter_combinations("")
    print letter_combinations("6789")
    items = [range(1,101)]
    nodes = [ListNode(i) for i in range(1,101)]
    list1 = nodes[0]
    list1.append(nodes[10])
    print "list1: %s"%list1
    list2 = nodes[2]
    list2.append(nodes[4])
    print "list2: %s"%list2
    list3 = nodes[3]
    list3.append(nodes[5])
    list3.append(nodes[6])
    list3.append(nodes[7])
    print "list3: %s"%list3
    print merge_k_lists([list1,list2,list3])
    print merge_k_lists([[],[]])

    print "all tests passed"
