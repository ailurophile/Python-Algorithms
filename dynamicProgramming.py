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


if __name__ == '__main__':
    print number_of_paths(5)
    print number_of_paths(-4)
    print number_of_paths(0)
    print number_of_paths(6)
