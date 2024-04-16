#game

matrix = [[1 if i < 2 or i >= 6 else 0 for j in range(8)] for i in range(8)]

for row in matrix:
    print(row)