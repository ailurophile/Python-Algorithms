from collections import defaultdict
def word_count_engine(document):
    """Implement a document scanning function wordCountEngine,
     which receives a string document and returns a list of all
     unique words in it and their number of occurrences,
     sorted by the number of occurrences in a descending order.
      Assume that all letters are in english alphabet. Your function
       should be case-insensitive, so for instance, the words Perfect
        and perfect should be considered the same word.
        The engine should strip out punctuation (even in the middle of a word)
        and use whitespaces to separate words. Analyze the time and space
        complexities of your solution. Try to optimize for time while keeping
        a polynomial space complexity."""

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
    print counts
    sum = 0
    for i in range(len(counts)):
        sum += counts[i]
        counts[i] = sum  #counts array now holds number of word frequencies equal to or smaller than index
#dimension output array
    print counts
    output = [("dummy",0) for _ in range(len(tuples)+1)]
    print "output = %s" % output
    for tuple in tuples:

        output[counts[tuple[1]]] = tuple
        counts[tuple[1]] -= 1
        print output
        print counts
    return output[1:]


if __name__ == '__main__':
  document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
  print word_count_engine(document)
