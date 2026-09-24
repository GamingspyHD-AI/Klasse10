matrix = [
    [1, 5, 8, 7],
    [2, 6, 9, 4],
    [3, 7, 10, 1],
    [4, 8, 11, 2]
]

finmat = []

for mem in range(len(matrix)):
    new_matrix = []
    for el in range(len(matrix[mem]) - 1, -1, -1):
        new_matrix.append(matrix[el][mem])
    finmat.append(new_matrix)

for zeile in finmat:
    print(zeile)