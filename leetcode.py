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


if __name__ == '__main__':
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("abcdef") == 6
    assert length_of_longest_substring("abbb") == 2
    assert length_of_longest_substring("abcabcde") == 5
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("anviaj") == 5


    print "all tests passed"
