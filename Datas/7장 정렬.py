# 선택정렬
def selection_sort(a):
    for i in range(0, len(a) - 1):
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > a[j]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]


a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬전:\t', end='')
print(a)
selection_sort(a)
print('정렬후:\t', end='')
print(a)


# %%

# 삽입정렬
def insertion_sort(a):
    for i in range(1, len(a) - 1):
        for j in range(i, 0, -1):
            if a[j - 1] > a[j]:
                a[j], a[j - 1] = a[j - 1], a[j]


a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬전:\t', end='')
print(a)
selection_sort(a)
print('정렬후:\t', end='')
print(a)

# 쉘정렬
def shell_sort(a):
    h = 4
    while h >= 1:
        for i in range(h, len(a)):
            j = i
            while j >= h and a[j] < a[j - h]:
                a[j], a[j - h] = a[j - h], a[j]
                j -= h
        h //= 3


a = [65, 95, 90, 80, 55, 70, 35, 50, 10, 20, 40, 30]
print('정렬전:\t', end='')
print(a)
selection_sort(a)
print('정렬후:\t', end='')
print(a)

# 힙정렬
def downheap(i, size):
    while 2 * i <= size:
        k = 2 * i
        if k < size and a[k] < a[k + 1]:
            k += 1
        if a[k] < a[i]:
            break
        a[i], a[k] = a[k], a[i]
        i = k


def create_heap(a):
    hsize = len(a) - 1
    for i in range(1, hsize // 2 + 1):
        downheap(i, hsize)


def heap_sort(a):
    N = len(a) - 1
    for i in range(N):
        a[1], a[N] = a[N], a[1]
        downheap(1, N - 1)
        N -= 1


a = [-1, 65, 95, 90, 80, 55, 70, 35, 50, 10, 20, 40, 30]
print('정렬전:\t', end='')
print(a)
print('최대힙:\t', end='')
create_heap(a)
print(a)
print('정렬후:\t', end='')
heap_sort(a)
print(a)

# 합병 정렬
CALL_SIZE = 7


def insertion_sort(a, low, high):
    for i in range(low, high):
        for j in range(len(a) - 1, i, -1):
            if a[j] < a[j - 1]:
                a[j - 1], a[j] = a[j], a[j - 1]


def merge(a, b, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high + 1):
        if i > mid:
            b[k] = a[j]
            j += 1
            a[k] = b[k]
        elif j > high:
            b[k] = a[i]
            i += 1
            a[k] = b[k]
        elif a[i] < a[j]:
            b[k] = a[i]
            i += 1
            a[k] = b[k]
        else:
            b[k] = a[j]
            j += 1
            a[k] = b[k]


def merge_sort(a, b, low, high):
    if high <= low + CALL_SIZE:
        insertion_sort(a, low, high)
        return
    mid = (low + high) // 2
    merge_sort(a, b, low, mid)
    merge_sort(a, b, mid + 1, high)
    if a[mid] <= a[mid + 1]:
        return
    merge(a, b, low, mid, high)


a = [65, 95, 90, 80, 55, 70, 35, 50, 10, 20, 40, 30]
b = [None] * len(a)
print('정렬전:\t', end='')
print(a)
merge_sort(a, b, 0, len(a) - 1)
print('정렬후:\t', end='')
print(a)

# 퀵정렬
def insertion_sort(a, low, high):
    for i in range(low, high):
        for j in range(len(a) - 1, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]


def qsort(a, low, high):
    Call_Size = 7
    if low <= high + Call_Size:
        insertion_sort(a, low, high)
        return
    else:
        pivot = partition(a, low, high)
        qsort(a, pivot + 1, high)
        qsort(a, low, pivot - 1)


def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    a[pivot], a[j] = a[j], a[pivot]
    return j


a = [65, 95, 90, 80, 55, 70, 35, 50, 10, 20, 40, 30]
print('정렬전:\t', end='')
print(a)
qsort(a, 0, len(a) - 1)
print('정렬후:\t', end='')
print(a)


# 기수정렬
def lsd_sort(a):
    WIDTH = 3
    N = len(a)
    R = 128
    temp = [None] * N
    for d in range(2, -1, -1):
        count = [0] * (R + 1)
        for i in range(N):
            count[ord(a[i][d]) + 1] += 1
        for j in range(1, R):
            count[j] += count[j - 1]
        for i in range(N):
            p = ord(a[i][d])
            temp[count[p]] = a[i]
            count[p] += 1
        for i in range(N):
            a[i] = temp[i]
        print('%d번째 문자:\t' % d, end='')
        for x in a: print(x, ' ', end='')
        print()


a = ['ICN', 'SFO', 'LAX', 'FRA', 'SIN', 'ROM', 'HKG', 'TLV', 'SYD', 'MEX', 'LHR', 'NRT', 'JFK', 'PEK', 'BEP', 'MOW']
print('정렬전:\t\t', end='')
for x in a: print(x, ' ', end='')
print()
lsd_sort(a)


# 반복합병정렬
def merge(left, right):
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergesort(list):
    if len(list) < 2:
        return list

    middle = len(list) // 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)


seq = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(seq);
print("\n")
print("Sorted array is")

print(mergesort(seq))