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
    count_coins(value,coins,0, counts)
    return counts[value]

def count_coins(value,coins,index, counts):
    if counts[value] != 0:
        return counts[value]
    coin = coins[index]
    if coin == 1:
        return 1  #only one way to make value using pennies
    index += 1
    count = 0
    for i in range(value/coin):
        count += count_coins(value - i*coin, coins, index, counts)
    count += count_coins(value%coin, coins, index, counts)
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

        if row == 7:
            paths.append(queens_array + [(row,column)])#valid placement of 8 found
            return
#        #get placement for next row
        for col in range(8):
            placement = place_queens(queens_array + [(row,column)], row + 1, col, paths)



def is_path_clear(array, row, column):
    """returns false if an entry is array shares a row, column or diagonal with (row,column)
    else returns True"""
    for spot in array:
        if spot[0] == row or spot[1] == column:
            return False
        if abs(spot[0] - row) == abs(spot[1] - column):
            return False
    return True



if __name__ == '__main__':
    placements = queen_placements()
    print "placement count = %d" % len(placements)
    print placements
    print("testing coins")
    print count_coins_to_value(12)
    print count_coins_to_value(10)
    print count_coins_to_value(1)
    print count_coins_to_value(5)
    print count_coins_to_value(32)
