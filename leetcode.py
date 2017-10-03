from collections import Counter

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
def is_match(input_string,pattern):
    """
    . matches any character
    * matches zero or more occurences of previous character
    Inputs: string to parse, pattern to use for comparison
    Output: boolean, true if pattern matches
    """

    def remove_dups(full_pattern):
        def remove_extra_asterisks(index):
            #returns number of asterisks beginning at index of pattern
            count = 0
            while index < length:
                if full_pattern[index] == "*":
                    count += 1
                    index += 1
                else:
                    break
            return count
        #beginning of remove_dups method
        no_dups = []
        i = 0
        length = len(full_pattern)
        #remove leading asterisks if any
#        if full_pattern[0] == "*":
#            i += 1 + remove_extra_asterisks(i+1)
        while i < length:
            #remove consecutive .* patterns
            if i+1 < length and full_pattern[i:i+2] == ".*":
                no_dups.extend(full_pattern[i:i+2])
                i += 2 + remove_extra_asterisks(i+2)
                while (i+1) < length  and full_pattern[i:i+2] == ".*":
                    i += 2 + remove_extra_asterisks(i+2)
            #remove consecutive *s
            elif full_pattern[i] == "*":
                no_dups.append("*")
                i += 1 + remove_extra_asterisks(i+1)
            else:
                #append character to search pattern
                no_dups.append(full_pattern[i])
                i+= 1
        return "".join(no_dups)
    #beginning of is_match
    s_length = len(input_string)
    pattern = remove_dups(pattern)
    p_length = len(pattern)
    s_index = 0
    p_index = 0
    if p_length == 0:
        return s_length == 0
    if s_length == 0 or pattern[0] == "*":
        return False
#        return pattern == "*"
    #process entire pattern string
    while p_index < p_length and s_index < s_length:
        pattern_character = pattern[p_index]
        if p_index +1 < p_length and pattern[p_index:p_index+2] == ".*":
        #skip any number of any characters
            p_index += 2
            if p_index == p_length:
                return True  #match to end of string
            #count required number of characters before matching next character
            number_of_characters_to_follow = 0
            while p_index < p_length and (pattern[p_index] == "." or pattern[p_index] == "*"):
                if pattern[p_index] == ".":
                    number_of_characters_to_follow += 1
                else:
                    number_of_characters_to_follow -= 1
                p_index += 1

            #find all occurences of next character to match
            character_to_seek = pattern[p_index]
            character_indices = [i for i,c in enumerate(input_string) if (c ==
            character_to_seek and i >= s_index+number_of_characters_to_follow)]
            for match in character_indices:
                if is_match(input_string[match:],pattern[p_index:]):
                    return True
            return False

        elif pattern_character == ".":
            s_index += 1 #match any single character
            p_index += 1
        elif pattern_character == "*": #match any number of the previous character
            character_to_skip = pattern[p_index-1]
            p_index += 1
            while s_index < s_length and input_string[s_index] == character_to_skip:
                s_index += 1
            if s_index == s_length: #string processed, if more pattern remains False
                return p_index == p_length
        else:
            if input_string[s_index] != pattern_character:
                return False
            s_index += 1
            p_index += 1
    #False if either have characters to process still
    return p_index == p_length and s_index == s_length

def least_intervals(jobs,recovery):
    """
    Input: array of letters [A:Z] representing jobs each taking 1
    unit of time to complete. Integer recovery indicating the number of intervals
    before another job of the same type can run.
    Output: Integer representing the fewest intervals required to run all jobs.
    """
    all_jobs = len(jobs)
    if all_jobs == 0:
        return 0
    if recovery < 0:
        return -1 #negative recovery time invalid
    counts = Counter(jobs)
    max_count = counts.most_common(1)[0][1]
    other_job_types = len(counts) - 1
    #are there enough job types to execute with no waiting?
    wait_intervals = (max_count-1)*recovery
    if wait_intervals <= other_job_types:
        return all_jobs #time required to process all jobs with no idling
    #determine how many jobs can run during recovery times
    sorted_counts = counts.most_common()
    sorted_counts.pop(0) #already placing most common job first
    during_recovery = 0
    wait_slots = max_count - 1
    for job,num in sorted_counts:
        during_recovery += min(wait_slots,num)
        if during_recovery >= wait_intervals:
            break
    return wait_intervals + all_jobs - min(during_recovery,wait_intervals)


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
    assert is_match("abc","a*b.") == True
    assert is_match("abc","abc") == True
    assert is_match("abc","a*****b.*.*") == True
    assert is_match("abc","*a*****b.*.*") == False
    assert is_match("abc",".*****.*.*") == True
    assert is_match("abcd","a*b.") == False
    assert is_match("abcd","a*b.*") == True
    assert is_match(".",".") == True
    assert is_match("r",".") == True
    assert is_match("rv",".") == False
    assert is_match(".","*") == False
    assert is_match("",".*") == False
    assert is_match("abcdabaja","a.*a") == True
    assert is_match("abcdabaja","a.*...a") == True
    assert is_match("abcdabaja","a.*...d.*") == False
    assert is_match("abcdabaja","a.*...*d.*") == True
    assert is_match("abcdabaja","a.*.ja") == True
    assert is_match("abcdabaja","a.*ja") == True
    assert least_intervals(['A','A','B','B','A'],1) == 5
    assert least_intervals(['A','A','B','B','A'],2) == 7
    assert least_intervals(['A','A','B','B','A'],0) == 5
    assert least_intervals(['A','A','B','B','A'],3) == 9
    assert least_intervals(['A','A','B','B','A','B'],1) == 6
    assert least_intervals(['A','A','B','B','A','B'],2) == 8
    assert least_intervals(['A','A','B','B','A','B'],3) == 10
    assert least_intervals(['A','A','B','B','A','B','C','D','E'],1) == 9
    assert least_intervals(['A','A','B','B','A','B','C','D','E'],2) == 9
    assert least_intervals(['A','A','B','B','A','B','C','D','E'],3) == 10
    assert least_intervals(['A','A','B','B','A','B','C','D','E'],4) == 12
    assert least_intervals( ['G','C','A','H','A','G','G','F','G','J','H','C','A',
    'G','E','A','H','E','F','D','B','D','H','H','E','G','F','B','C','G','F','H',
    'J','F','A','C','G','D','I','J','A','G','D','F','B','F','H','I','G','J','G',
    'H','F','E','H','J','C','E','H','F','C','E','F','H','H','I','G','A','G','D',
    'C','B','I','D','B','C','J','I','B','G','C','H','D','I','A','B','A','J','C',
    'E','B','F','B','J','J','D','D','H','I','I','B','A','E','H','J','J','A','J',
    'E','H','G','B','F','C','H','C','B','J','B','A','H','B','D','I','F','A','E',
    'J','H','C','E','G','F','G','B','G','C','G','A','H','E','F','H','F','C','G',
    'B','I','E','B','J','D','B','B','G','C','A','J','B','J','J','F','J','C','A',
    'G','J','E','G','J','C','D','D','A','I','A','J','F','H','J','D','D','D','C',
    'E','D','D','F','B','A','J','D','I','H','B','A','F','E','B','J','A','H','D',
    'E','I','B','H','C','C','C','G','C','B','E','A','G','H','H','A','I','A','B',
    'A','D','A','I','E','C','C','D','A','B','H','D','E','C','A','H','B','I','A',
    'B','E','H','C','B','A','D','H','E','J','B','J','A','B','G','J','J','F','F',
    'H','I','A','H','F','C','H','D','H','C','C','E','I','G','J','H','D','E','I',
    'J','C','C','H','J','C','G','I','E','D','E','H','J','A','H','D','A','B','F',
    'I','F','J','J','H','D','I','C','G','J','C','C','D','B','E','B','E','B','G',
    'B','A','C','F','E','H','B','D','C','H','F','A','I','A','E','J','F','A','E',
    'B','I','G','H','D','B','F','D','B','I','B','E','D','I','D','F','A','E','H',
    'B','I','G','F','D','E','B','E','C','C','C','J','J','C','H','I','B','H','F',
    'H','F','D','J','D','D','H','H','C','D','A','J','D','F','D','G','B','I','F',
    'J','J','C','C','I','F','G','F','C','E','G','E','F','D','A','I','I','H','G',
    'H','H','A','J','D','J','G','F','G','E','E','A','H','B','G','A','J','J','E',
    'I','H','A','G','E','C','D','I','B','E','A','G','A','C','E','B','J','C','B',
    'A','D','J','E','J','I','F','F','C','B','I','H','C','F','B','C','G','D','A',
    'A','B','F','C','D','B','I','I','H','H','J','A','F','J','F','J','F','H','G',
    'F','D','J','G','I','E','B','C','G','I','F','F','J','H','H','G','A','A','J',
    'C','G','F','B','A','A','E','E','A','E','I','G','F','D','B','I','F','A','B',
    'J','F','F','J','B','F','J','F','J','F','I','E','J','H','D','G','G','D','F',
    'G','B','J','F','J','A','J','E','G','H','I','E','G','D','I','B','D','J','A',
    'A','G','A','I','I','A','A','I','I','H','E','C','A','G','I','F','F','C','D',
    'J','J','I','A','A','F','C','J','G','C','C','H','E','A','H','F','B','J','G',
    'I','A','A','H','G','B','E','G','D','I','C','G','J','C','C','I','H','B','D',
    'J','H','B','J','H','B','F','J','E','J','A','G','H','B','E','H','B','F','F',
    'H','E','B','E','G','H','J','G','J','B','H','C','H','A','A','B','E','I','H',
    'B','I','D','J','J','C','D','G','I','J','G','J','D','F','J','E','F','D','E',
    'B','D','B','C','B','B','C','C','I','F','D','E','I','G','G','I','B','H','G',
    'J','A','A','H','I','I','H','A','I','F','C','D','A','C','G','E','G','E','E',
    'H','D','C','G','D','I','A','G','G','D','A','H','H','I','F','E','I','A','D',
    'H','B','B','G','I','C','G','B','I','I','D','F','F','C','C','A','I','E','A',
    'E','J','A','H','C','D','A','C','B','G','H','G','J','G','I','H','B','A','C',
    'H','I','D','D','C','F','G','B','H','E','B','B','H','C','B','G','G','C','F',
    'B','E','J','B','B','I','D','H','D','I','I','A','A','H','G','F','B','J','F',
    'D','E','G','F','A','G','G','D','A','B','B','B','J','A','F','H','H','D','C',
    'J','I','A','H','G','C','J','I','F','J','C','A','E','C','H','J','H','H','F',
    'G','E','A','C','F','J','H','D','G','G','D','D','C','B','H','B','C','E','F',
    'B','D','J','H','J','J','J','A','F','F','D','E','F','C','I','B','H','H','D',
    'E','A','I','A','B','F','G','F','F','I','E','E','G','A','I','D','F','C','H',
    'E','C','G','H','F','F','H','J','H','G','A','E','H','B','G','G','D','D','D',
    'F','I','A','F','F','D','E','H','J','E','D','D','A','J','F','E','E','E','F',
    'I','D','A','F','F','J','E','I','J','D','D','G','A','C','G','G','I','E','G',
    'E','H','E','D','E','J','B','G','I','J','C','H','C','C','A','A','B','C','G',
    'B','D','I','D','E','H','J','J','B','F','E','J','H','H','I','G','B','D'],
    1) == 1000





    print "all tests passed"
