import time
m1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
m2= [
    [13,9,5,1],
    [14,10,6,2],
    [15,11,7,3],
    [16,12,8,4]
]
#m = [range(10000) for x in range(10000)]
#print m
def time_execution(code):
    
    start = time.clock()  # start the clock
    result = eval(code)  # evaluate any string as if it is a Python command
    run_time = time.clock() - start  # find difference in start and end time
    return run_time
#   return result, run_time  # return the result of the code and time taken

def rotate(matrix):
    n=len(matrix[0])
    for row in range(0,n):
        for i in range(row,n-1-row):
            temp = matrix[row][i]
            matrix[row][i] = matrix[n-1-i][row]
            matrix[n-1-i][row] = matrix[n-1-row][n-1-i]
            matrix[n-1-row][n-1-i] = matrix[i][n-1-row]
            matrix[i][n-1-row] = temp
            #print matrix
    return matrix
def listrotate(matrix):
    n = len(matrix[0])
#    m=[[row[n-1-i] for row in matrix] for i in range(n-1,-1,-1)] #-90degrees
    m = [[matrix[col][row] for col in range(n-1,-1,-1)] for row in range(0,n)]
    return m 

def buildOrder(projects,dependencies):
    order = []
    D = {}
    # build graph
    for p,d in dependencies:
        if p not in D:
            D[p] = {'precursors':1,'waiters':[]}
        else:
            D[p]['precursors'] += 1
        if d not in D:
            D[d] = {'precursors':0, 'waiters':[p]}
        else:
            (D[d]['waiters']).append(p)
    #schedule jobs with no dependencies 
    for p in projects:
        if p not in D:
            order.append(p)   
    scheduled = len(order)
    while len(order) < len(projects):
        scheduled = []
        for proj in D:
            if proj not in order and (D[proj]['precursors'] == 0):              
                scheduled.append(proj)
                for job in D[proj]['waiters']:
                    D[job]['precursors'] -= 1
        order.extend(scheduled)
        if len(scheduled) == 0:
            return "ERROR"
        
    return order

def countOnes(num):
    if num == 0 or num == None:
        return [0]
    runs = []
    sum = 0
    for i in range(num.bit_length()):
        if num % 2 == 1:
            sum += 1
        elif sum != 0:
            runs.extend([sum,0])
            sum = 0
        else:
            runs.append(0)
        num = num>>1
    if sum != 0:
        runs.append(sum)
    #print runs
    return runs

def flipBit(num):
    if num == None: return 0
    if num == 0: return 1
    most = 0
    sequences = countOnes(num)
    i = 0
    while (i+2) < len(sequences):
        count = sequences[i] + sequences[i+1] + sequences[i+2] +1
        most = max(most,count)
        #advance to next non-zero entry
        while True:
            i += 1
            if i >= (len(sequences) or sequences[i]) != 0:
                break
    #process final entries
    count = 0
    if len(sequences) < 3:
        count = sum(sequences)+1
        if len(sequences) == 1:
            count -= 1  #adjust for all 1s case
    else:
        count = sequences[-1] + sequences[-3] + sequences[-2] +1
    most = max(most,count)
    return most

def getNext(start):
    num = start
    if (num<=0):
        return None, None
    bits = num.bit_length()
    highestOne = -1
    secondHighestOne = -1 
    secondZero = -1
    firstOneAfterZero = -1
    bit = 0
    while (num%2 ==1) and (bit<bits) :
        num = num >> 1
        bit += 1
    if bit == bits:  #all 1s
        higher = start - (1<<(bits-1)) + (1<<bits)
        return None, higher
    lowestZero = bit
    while (bit<bits) and (num%2 ==0):
        num = num >> 1
        bit += 1
        #print "bit = %s num = %s" % (bit, num)
    firstOneAfterZero = bit 
    highestOne = bit
    num = num>>1
    bit += 1
    while (bit<bits):
        if num%2 == 1:
            secondHighestOne = highestOne
            highestOne = bit 
            num = num>>1
            bit += 1
        else:
            if secondZero == -1:
                secondZero = bit
            num = num >> 1
            bit += 1
    smaller = start - (1<<firstOneAfterZero) + (1<<(firstOneAfterZero-1))
    if secondZero == -1:
        #print start
        #print 1<<(highestOne+1)
        #print (1 << highestOne)
        #print 1<<lowestZero
        #print (1<<firstOneAfterZero)
        #bigger = start + 2**(highestOne + 1) - 2**highestOne
        bigger = start + (1<<(highestOne+1)) - (1<<highestOne) 
        #print bigger
        if secondHighestOne != -1:
            #print '2nd highest 1 found'
            bigger = bigger - (1<<secondHighestOne) + (1<<lowestZero)
    else:
        bigger = start + 2**secondZero - (2**firstOneAfterZero)
    return smaller,bigger

def fibonacci(n):
    fib = [0,1]
    if n <2:
        return fib[n]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib.pop()
def memofib(n,array):
    if n < 2:
        return n
    if array[n] == 0:
        array[n] = memofib(n-1,array) + memofib(n-2,array)
    return array[n]
def recfib(n):
    if n < 2:
        return n
    memo = [0 for i in range(n+1)]
    memo[1] = 1
    return memofib(n,memo)
def merge(res,perms):
    if res == []:
        return perms
    return [l+p for l in res for p in perms]
def stairs(n,results):
    
    if n > 3:
        a = merge([(1,)],stairs(n-1,results))
        b = merge([(2,)],stairs(n-2,results))
        c = merge([(3,)],stairs(n-3,results))
        #print a,b,c
        results = a+b+c
        return results
    if n < 1:
        return results
    if n == 1:
        return merge(results,[(1,)])
    if n == 2:
        return merge(results,[(1,1),(2,)])
    if n == 3:
        return merge(results,[(1,1,1),(1,2), (2,1),(3,)])
def countStairs(n,res=0):
    if n < 1:
        return res
    if n == 1:
        return 1+res
    if n == 2:
        return 2+res
    if n == 3:
        return 4+res
    return countStairs(n-1,res) + countStairs(n-2,res) +countStairs(n-3,res) 
def row(pair): return pair[0]
def col(pair): return pair[1]
def memoRobots(r,c,grid,path=[],visited=[]):
    if (r<0) or (c<0):
        return False    
    if path == []:
        current = (0,0)
    else:
        current = path[-1]
    if current == (r,c): 
        if (grid[row(current)][col(current)] == 1):
            return path
        else:
            return None
    down = (row(current)+1,col(current))
    right = (row(current),col(current)+1)
    for step in (down,right):
        
        if (((row(step) <= r) and (step == down)) or ((step == right) and (col(step) <= c))) and (grid[row(step)][col(step)] == 1):
            if step not in visited:
                visited.append(step)
                path.append(step)        
                check = memoRobots(r,c,grid,path,visited)
                if check != None:
                    return check
                else:
                    path.pop()
    return None
"""
def memoRobot(r,c,grid,path=[],visited=[]):
    if (r<0) or (c<0):
        return False
    
    if path == []:
        current = (0,0)
    else:
        current = path[-1]
    if current == (r,c) and (grid[current[0]][current[1]] == 1):
        return path
    down = (current[0]+1,current[1])
    right = (current[0],current[1]+1) 
    if (down[0] <= r) and (grid[down[0]][down[1]] == 1):
        if down not in visited:
            visited.append(down)
            path.append(down)        
            check = memoRobot(r,c,grid,path,visited)
            if check != None:
                return check
            else:
                path.pop()
    if (right[1] <= c) and (grid[right[0]][right[1]] == 1):
        path.append(right)       
        check = memoRobot(r,c,grid,path,visited)
        if check != None:
            return check
        else:
            path.pop()
    return None
"""    
def robot(grid):
    r = len(grid) - 1
    c = len(grid[0]) - 1
    path = [(0,0)]
    #visited = []
    return memoRobots(r,c,grid,path,[])
def isPath(r,c,grid,current=(0,0)):
    if (r<0) or (c<0):
        return False

    if current == (r,c) and (grid[current[0]][current[1]] == 1):
        return True
    down = (current[0]+1,current[1])
    right = (current[0],current[1]+1)  
    
    
    if (down[0] <= r) and (grid[down[0]][down[1]] == 1):
        if down == (r,c):
            return True
        if isPath(r,c,grid,down):
            return True
    if (right[1] <= c and grid[right[0]][right[1]] == 1):
        if right == (r,c):
            return True
        if isPath(r,c,grid,right):
            return True
    return False
def mult(fewer,more,result):
    if fewer == 0:
        return result
    if fewer&1 == 1:
        result += more
    fewer = fewer>>1
    more = more<<1
    return mult(fewer,more,result)
def multiply(x,y):
    acount=0
    a=x
    b=y
    bcount=0
    while a>0:
        acount +=1
        a = a&(a-1)
    while b>0:
        bcount +=1
        b = b&(b-1)
    if acount<bcount:
        print "%s has fewer 1s"%x
        return mult(x,y,0)
    else:
        return mult(y,x,0)
def subsets(s):
    def merge(item,subsets):
        output = [[item]]
        for s in subsets:
            output.append(s)
            t = s + [item]
            output.append(t)
        return output
    if len(s) < 2: return [s]
    member = s.pop()
    return merge(member,subsets(s))

def permsWithoutDups(string):
    listString = list(string)
    #listString.sort()
    #output = perms(listString)
    output = bups(listString)
    outstrings = []
    for s in output:
        outstrings.append("".join(s))
    return outstrings
def mergeAll(item,lists):
    #print item,lists
    for i in range(len(lists)-1,-1,-1):
        for pos in range(len(lists[i])):
            lists.append(lists[i][0:pos] + item + lists[i][pos:] )
        lists.append(lists[i]+item)
        lists.pop(i)
    noDups=dict.fromkeys(lists,0)
    return noDups.keys()
def perms(string):
    #print string
    if len(string) <2:
        return [string]
    return mergeAll(string[0:1], perms(string[1:]))
def mergePerms(item,d):
    #print item,lists
    newPerms = {}
    shortPerms = d.keys()
    for perm in d:
        for pos in range(len(perm)):
            newPerm = perm[0:pos] + item + perm[pos:]
            if newPerm not in d:
                newPerms[newPerm] = 1
        newPerms[perm+item] = 1  
    for perm in shortPerms:
        d.pop(perm)
    d.update(newPerms)
    return d
def permsWithDups(string):
    #print string
    if len(string) <2:
        return {string:1}
    fewer= permsWithDups(string[1:])
    return mergePerms(string[0:1], fewer )
def permutations(string):
    d = permsWithDups(string)
    return d.keys()
if __name__ == '__main__':
    #print bups(['a','b','c'])
    #print perms('a')
    print permutations('lisa')
    #print perms('lisa')
    print permutations('lila')
    print permutations('lill')
    print permutations('lili')
    #print mergeAll('a',[['b'],['x','y']])
    """
    print perms(['a','b'])
    print perms(['a','b','c'])
    print permsWithoutDups('lisa')
    
    print mult(2,13,0)
    print multiply(7,5)
    
    #s = set([1,2,3])
    print subsets([1,2,3,4])
    m = [[1 for i in range(3)]for j in range(3)]
    #print robot(m)
    m[1]=[0,0,1]
    #m[2] = [1,1,0]
    #print robot(m)
    n = [[1,1,1,1],[1,1,0,1],[1,1,0,1],[0,1,0,1]]
    #print robot(n)
   
    #print isPath(len(m)-1,len(m[0])-1,m,(0,1))
    
    print stairs(6,[])
    print countStairs(6)
    
    for i in range(10):
        print fibonacci(i)
        print recfib(i)

    
    print getNext(2)
    print getNext(6)
    print getNext(18)
    print getNext(0)
    for i in range(33):
        lo,hi = getNext(i)
        if lo != None:
            print (bin(lo),bin(i))
        else:
            print (lo,i)
        if hi != None:
            print bin(hi)
        else:
            print hi



    
    print flipBit(5)
    print flipBit(0)
    print flipBit(~0)
    print flipBit(0b01110101101)
#print rotate(m)
#print [row for row in listrotate(m)]
#print [row for row in rotate(m)]
#print time_execution('rotate(m)')
#print time_execution('listrotate(m)')

    p = ['a','b','c','d','e','f']
    d = [('d','a'),('b','f'),('d','b'),('a','f'),('c','d')] #1st depends on 2nd
    e = [('e','a'),('b','f'),('e','b'),('a','b'),('c','f'),('a','c'),('a','f'),('g','d')]
    print buildOrder(p,e)

print m
m = listrotate(m)
print m



def compress(A):
    out = []
    L = list(A)
    i = 0
    while i< len(A):
        c = A[i]
        out.append(c)
        #print out
        count = 1
        j = i+1
        while j<len(A):
            if A[j] == A[i]:
                count +=1
                j+=1
            else:
                break
        i+= count
        out.append(str(count))
        
    if len(out) < len(A):
        return ''.join(out)
    return A
    
A = 'aaaaaaaabcccccccddfghh'
B = 'aabcde'
print compress(A)
print compress(B)
"""