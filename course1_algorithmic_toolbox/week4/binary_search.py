

def binary_search(list, key):
    if not list:
        return -1
    mid = int(len(list) / 2)
    if list[mid] == key:
        return 'Found'
    if list[mid] < key:
        return binary_search(list[mid + 1:], key)
    else:
        return binary_search(list[:mid], key)

print(binary_search([1,3,4,5,6,7], 5))
print(binary_search([1,3,4,5,6,7], 50))