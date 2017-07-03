def selection_sort(n):
    for i in range(len(n)):
        minIndex = i
        for j in range(i+1, len(n)):
            if n[j] < n[minIndex]:
                minIndex = j
        n[i], n[minIndex] = n[minIndex], n[i]
    return n


print(selection_sort([4, 3, 2, 1]))


def merge(a, b):
    d = list()
    index_a, index_b = 0, 0
    while index_a < len(a) and index_b < len(b):
        el_a = a[index_a]
        el_b = b[index_b]
        if el_a <= el_b:
            d.append(el_a)
            index_a += 1
        else:
            d.append(el_b)
            index_b += 1

    d.extend(a[index_a:])
    d.extend(b[index_b:])
    return d


def merge_sort(n):
    if len(n) == 1:
        return n
    mid = int(len(n) / 2)
    left_half = merge_sort(n[:mid])
    right_half = merge_sort(n[mid:])
    return merge(left_half, right_half)


print(merge_sort([4, 3, 2, 1]))
print(merge_sort([8, 9, 1, 2]))


print(merge([1, 3, 2, 5, 4], [5, 6, 7, 8, 9]))


def partition(n1):
    random_pivot = 0
    pivot = n1[random_pivot]
    index_less = random_pivot
    for i in range(random_pivot + 1, len(n1)):
        if n1[i] <= pivot:
            index_less += 1
            n1[index_less], n1[i] = n1[i], n1[index_less]
    n1[random_pivot], n1[index_less] = n1[index_less], n1[random_pivot]
    return index_less

def quick_sort(n):
    if len(n) <= 1:
        return n
    m = partition(n)
    quick_sort(n[:m])
    quick_sort(n[m+1:])

n = [1, 3, 2, 5, 4, 5, 6, 7, 8, 9]
# quick_sort(n)
print(quick_sort(n))