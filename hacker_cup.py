import math
def lazy_loader(filename):
    """Wilson works for a moving company. His primary duty is to load household
    items into a moving truck. Wilson has a bag that he uses to move these items.
    He puts a bunch of items in the bag, moves them to the truck, and then drops
    the items off. Wilson has a bit of a reputation as a lazy worker. Julie is
    Wilson's supervisor, and she's keen to make sure that he doesn't slack off.
    She wants Wilson to carry at least 50 pounds of items in his bag every time
    he goes to the truck.Luckily for Wilson, his bag is opaque. When he carries
    a bagful of items, Julie can tell how many items are in the bag (based on
    the height of the stack in the bag), and she can tell the weight of the top
    item. She can't, however, tell how much the other items in the bag weigh.
    She assumes that every item in the bag weighs at least as much as this top
    item, because surely Wilson, as lazy as he is, would at least not be so
    dense as to put heavier items on top of lighter ones. Alas, Julie is woefully
    ignorant of the extent of Wilson's lack of dedication to his duty, and this
    assumption is frequently incorrect.Today there are N items to be moved, and
    Wilson, paid by the hour as he is, wants to maximize the number of trips he
    makes to move all of them to the truck. What is the maximum number of trips
    Wilson can make without getting berated by Julie? Note that Julie is not
    aware of what items are to be moved today, and she is not keeping track of
    what Wilson has already moved when she examines each bag of items. She simply
    assumes that each bagful contains a total weight of at least k * w where k
    is the number of items in the bag, and w is the weight of the top item.

    Input

    Input begins with an integer T, the number of days Wilson "works" at his job.
    For each day, there is first a line containing the integer N. Then there are
    N lines, the ith of which contains a single integer, the weight of the ith
    item, Wi.

    Output

    For the ith day, print a line containing "Case #i: " followed by the maximum
    number of trips Wilson can take that day.

    Constraints
    range T [1,500]
    range N,Wi [1,100]
    On every day, it is guaranteed that the total weight of all of the items is
    at least 50 pounds.


    """
    try:
        with open(filename,'r') as input_file:

            days = input_file.readline()
            for i in range(int(days)):
                N = input_file.readline()
                items = []
                for _ in range(int(N)):
                    items.append(int(input_file.readline()))
                quicksort(items)
                trips = 0
                while len(items) > 0:
                    weight = items.pop(0)
                    if weight >= 50:
                        trips += 1  #carry just the heavy items
                    else:
                        load = int(math.ceil(50.0/weight))
                        if load-1 > len(items):  #weight is 1 item in load
                            del items[0:] #insufficient load so empty array
                        else:
                            trips += 1  #viable load so add to trip count
                            del items[-1*(load-1):] # remove rest of load
                print "Case #%s: %s" % (i+1,trips)
    except Exception,e:
        print "Encountered an Exception: " + str(type(e))

def quicksort(array):
    if array == None or len(array) < 2:
        return
    quick_sort(array, 0, len(array) - 1)

def quick_sort(array, start, end):
    if array == None or len(array) < 2 or start > end:
        return
    front_index = start
    back_index = end
    pivot_value = array[back_index]
    while front_index < back_index:
        if array[front_index] < pivot_value:
            #value larger than pivot_value so swap
            array[back_index] = array[front_index]
            back_index -= 1
            array[front_index] = array[back_index]
        else:
            front_index += 1
    array[front_index] = pivot_value
    quick_sort(array,start,front_index-1)
    quick_sort(array,front_index+1, end)




if __name__ == "__main__":
    lazy_loader("lazy_loading.txt")
