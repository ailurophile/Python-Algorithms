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

if __name__ == '__main__':
  document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
  print word_count_engine(document)
  print word_counter_engine(document)
