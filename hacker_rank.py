def  oddNumbers(l, r):
    results = []
    if l%2 == 1:
        results.append(l)
        current = l+2
    else:
        current = l+1
    while current <= r:
        results.append(current)
        current += 2
    return results

def dnaComplement(s):
    complement = {"A":"T","T":"A","C":"G","G":"C"}
    results = []
    for letter in s[::-1]:
        results.append(complement[letter])
    return ''.join(results)
def longestChain(words):
    if len(words) <2:
        return len(words)
    buckets = [[] for _ in range(61)]
    for word in words:
        buckets[len(word)].append(word)
    chain_lengths = {}
    for each in buckets[1]:
        chain_lengths[each] = 1
    longest = 1
    for i in range(2,61):
        if len(buckets[i])==0:
            break
        for each in buckets[i]:
            length = len(each)
            for j in range(length):
                shorter = each[:j] + each[j+1:]
                if shorter in chain_lengths:
                    chain_lengths[each] = chain_lengths[shorter]+1
                    if chain_lengths[each] > longest:
                        longest = chain_lengths[each]


    return longest

if __name__ == '__main__':
    print oddNumbers(3,9)
    print dnaComplement("ACCGGGTTTT")
    print longestChain(["a","b","ba","bca"])
    print longestChain(["a","b","ba","bca","bdca"])
    print longestChain(["a","b","ba","bac"])
    print longestChain([])
