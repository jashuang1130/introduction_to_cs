def isPalindrome(string):
    palindrome = False
    reversed_string = ''.join(reversed(string))
    if string == reversed_string:
        palindrome = True
        return palindrome

isPalindrome('test')
isPalindrome('abbabba')

def rotationPalindrome(string):
    if isPalindrome(string):
        return True
    # Now try all rotations one by one
    n = len(string)
    for i in range(n-1):
        string1 = string[i + 1:n]
        string2 = string[0:i + 1]
        print(string1, string2)

        # Check if this rotation is palindrome
        string1+=(string2)
        print('final', string1)
        if isPalindrome(string1):
            return True
    return False

rotationPalindrome('abcba')


# SEARCHING AND SORTING
# time complexity O(log(n))
# 1 = n/2^i  => i = log n
def bisection_search(L, e):
    if L == []:
        # constant O(1)
        return False
    elif len(L) == 1:
        # constant O(1)
        return L[0] == e
    else:
        half = len(L)//2  # constant O(1)
        # recursive call O(nlog(n))
        if L[half] > e:
            return bisection_search(L[:half], e) # L[:half] makes a new list, slows down
        else:
            return bisection_search(L[half:], e)

def alternative_bisection_search(L, e):
    # Look at some list instead of creating new lists - doesn't need to copy lists
    # recursive is O(1)?
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, o, len(L) - 1)

# O() for iterative factorial = O(n)
def factorial_iterative(n):
    prod = 1
    for i in range(i, n+1):
        prod *= i
    return prod

# O() for recursive factorial = O(n); may take longer time but same order of growth
def factorial_recursive(n):
    '''assume n >= 0 '''
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Log Linear nLog(n) ex: merge sort

# Polynomial complexity O(n^2). common in nested loops or recursive function calls

# Exponential complexity O(2^n). Towers of Hanoi. WANT TO AVOID!!!
# recursive function where there is more than one recursive call for each size of problem

# Power set - given a set of integers (with no repeats),
# want to generate the collection of all possible subsets
# {1, 2, 3, 4} would generate (order doesn't matter)
# {}, {1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4},
# {1,2,3}, {1,2,4}, {1,3,4},{2,3,4},{1,2,3,4}

# power set of 0 = {}
# power set of 1 = {1}
# power set of 2 = {2}, {1,2}
# power set of 3 = {3}, {1,3}, {2,3}, {1,2,3}
# power set of 4 = {4}, {1,4}, {2,4}, {1,2,4},{3,4},{1,3,4},{2,3,4},{1,2,3,4}
def gen_power_subset(L):
    if len(L) == 0:
        return [[]] # list of empty list

    smaller = gen_power_subset(L[:-1]) # all subset without last element
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra) # for all smaller solutions, add one with last element

    return smaller+new # combine those with last element and those without

'''
SUMMARY:
    O(1) - code doesn't depend on size of problem
    O(log n) - reduce probblem in half each time through process
    O(n) - simple iterative or recursive programs
    O(n log n) Log Linear -
    O(n^c) - nested loops or recursive calls
    O(c^n) - multiple recursive calls at each level
'''

# Complexity of iterative fibonacci
def iterative_fibonacci(n):
    if n == 0:       # O(1)
        return 0
    elif n == 1:     # O(1)
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):   # O(n)
            temp = fib_i
            fib_i = fib_ii
            fib_ii = temp + fib_i
        return fib_ii

# Complexity of recursive fibonacci - exponential growth: golden ratio to nth power
def recursive_fibonacci(n):
    ''' assumes n an int >= 0 '''
    if n == 0:     # O(1)
        return 0
    elif n == 1:   # O(1)
        return 1
    else:   # O(2^n)
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

recursive_fibonacci(8)


# recursive vs dynamic programming: improve performance
# Similar to fibonacci
def recursive_num_ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return recursive_num_ways(n-1) + recursive_num_ways(n-2)

# num_ways from bottom up
def dynamic_num_ways(n):
    if n == 0 or n == 1:
        return 1
    nums = new int[n + 1]
    nums[0] = 1; nums[1] = 1
    for i from 2 upto n:
        num[i] = nums[i - 1] + nums[i - 2]
    return nums[n]


# Searching and Sorting Algorithms
# Search - find a item or group of items from a collection
# Log Linear Algorithm
# Linear Search O(n): Exausive Numeration/Brute-force (British Museum Algorithm) Search - go throug every options
#   - list doesn't need to be sorted
# Bisection Search O(log ns) - List MUST be sorted - keep splitting collection into smaller pieces

# When does it make sense to sort first then search?
# SORT + O(log n) < O(n) -> SORT < O(n) - O(log n)
# when sorting is less than O(n) NEVER TRUE!!!

# Amortized Cost - sort first then can be used for many of future searches
# SORT + K * O(log n ) < K * O(n) -> for large K, SORT time becomes irrelevant if cost of sorting is small enough

# Monkey Sort (Permutation Sort) aka. bogosort, stupid sort, slowsort, shotgun sort. scattered n^n
def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)
# best case: O(n); worst case O(?) n^n

# Bubble Sort   - compare consecutive pairs of elements, swap elements and start over hwne reaches the end of list.
#               - stop when no more swaps have been made
#               - largest will be at end of list
def bubble_sort(L): # at most n times through the list
    swap = False
    while not swap:
        swap = True
        for i in range(1, len(L)): # multiple passes until no more swaps
            if L[i-1] > L[i: # inner loop: comparison
                swap = False
                temp = L[i]
                L[i] = L[i-1]
                L[j-1] = temp

# Selection Sort - find smallest element and put it in front
#               1. extract min element, swap it w/ element at index 0
#               2. we know smallest is at 0; we then look at smalles from index of 1 to last and swap with 1
# Loop invariant
#   Base case: prefix empty, suffix while list - ivariant True
#   induction setp: move min element from suffix to end of prefix. since invariant true before move, prefix sorted after append
#   when exit, prefix is entire list, suffix fempty, so sorteds
def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

# Merge Sort - divide an conquer
# split list in half until have sublist of only one element
# merge sorted sublists. sublists will be sorted after merge

# Merging Sublists
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):  # everything that's left on the left-list. append to end
        result.append(left[i])
        i += 1
    while (j < len(right)): # everything that's left on the right-list. append to end
        result.append(right[j])
        j += 1
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

# divide list into halves
# depth-first such that conquer smallest pieces down one branch first before moving to larger pieces
