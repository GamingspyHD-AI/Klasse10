matrix = [[1, 5, 8],
          [3, 4, 7],
          [2, 9, 3]]

def pprint():
    for zeile in matrix:
        print(zeile)

def sprint():
    for zeile in matrix:
        for element in zeile:
            print(element)

sprint()