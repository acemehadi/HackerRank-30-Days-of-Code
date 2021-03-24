def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verifiy(index):
    if index is not None:
        print("Succesful we found", index)
    else:
        print("Not found")


list = [1, 2, 3, -4, 4, 5]
result = linear_search(list, 3)
verifiy(result)
