#Binary search test
def binarySearch(alist, find_item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == find_item:
            found = True
        else:
            if find_item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
list_test = [1,2,3,4,5,6,7,8]
print binarySearch(list_test, 9)
