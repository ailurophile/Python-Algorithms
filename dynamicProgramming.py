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


if __name__ == '__main__':
    print number_of_paths(5)
    print number_of_paths(-4)
    print number_of_paths(0)
    print number_of_paths(6)
    print("testing coins")
    print count_coins_to_value(12)
    print count_coins_to_value(10)
    print count_coins_to_value(1)
    print count_coins_to_value(5)
    print count_coins_to_value(32)
