# print("Practical-8 Conduction")
print("Searching:\n")
n, l = int(input("Enter No. of Elements: ")), []
print("Insert List: ")
for i in range(n):
    l.append(int(input()))

print("List:", l)


def BubbleSort(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i] < li[j]:
                li[i], li[j] = li[j], li[i]
    return li


def InsertionSort(li):
    for i in range(1, len(li)):
        temp = li[i]
        j = i - 1
        while j >= 0 and temp < li[j]:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp
    return li


def SelectionSort(li):
    for i in range(len(li)):
        min_idx = i
        for j in range(i + 1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j
        li[i], li[min_idx] = li[min_idx], li[i]
    return li


search = int(input("Enter Search Element: "))


def QuickSort(li, low, high):
    if len(li) == 1:
        print("Sorted List:", li)
        return li
    if low < high:
        i = (low - 1)
        pivot = li[high]
        for j in range(low, high):
            if li[j] <= pivot:
                i = i + 1
                li[i], li[j] = li[j], li[i]

        li[i + 1], li[high] = li[high], li[i + 1]
        pi = i + 1
        QuickSort(li, low, pi - 1)
        QuickSort(li, pi + 1, high)


def merge(li, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = li[l + i]

    for j in range(0, n2):
        R[j] = li[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            li[k] = L[i]
            i += 1
        else:
            li[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        li[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        li[k] = R[j]
        j += 1
        k += 1


def MergeSort(li, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        MergeSort(li, l, m)
        MergeSort(li, m + 1, r)
        merge(li, l, m, r)


def Linear(li, sear):
    flag = False
    for i in range(len(li)):
        if sear == li[i]:
            flag = True
            break

    result = [flag, i]
    if result[0]:
        print("Yes, Present at position: ", result[1])
    else:
        print("No, Not Present...")


def Binary(li, sear):
    BubbleSort(li)
    print("Sorted List:", li)
    low = 0
    high = len(li) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if li[mid] < sear:
            low = mid + 1
        elif li[mid] > sear:
            high = mid - 1
        else:
            return mid

    print("No, Not Present...")
    return -1


# Linear(l, search)

result = Binary(l, search)
if result != -1:
    print("Yes, Present at position: ", result)

# print("Bubble Sort:", BubbleSort(l))
# print("Insertion List:", InsertionSort(l))
# print("Selection List:", SelectionSort(l))

# QuickSort(l, 0, len(l) - 1)
# print("QuickSort List:", l)

# MergeSort(l, 0, len(l) - 1)
# print("Merge List:", l)


