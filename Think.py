books = []
books.append("C ")
books.append("C++ ")
books.append("Java  ")
books.append("python")


books.pop()
print("The top Book is", books[-1])

books.pop()
print("NOw the Book is ", books[-1])

books.pop()
print("YEs :the top book is ", books[-1])

books.pop()
print(books)


if not books:
    print("No Language Is no More")
