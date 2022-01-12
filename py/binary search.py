namess = ["Alan", "Bob", "Carl", "Danny", "Earl", "Frank"]
found = False
lengthh = len(namess)
search = input("")
counter = 0
mid = (lengthh//2)

while found == False:
    counter += 1
    if namess[mid] == search:
        found = True
    elif namess[mid] < search:
        mid = mid + 1
    elif namess[mid] > search:
        mid = mid - 1

print(counter)
