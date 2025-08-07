# matrix=[]
# for i in range(5):
#   row = list(map(int, input().split()))
#   matrix.append(row)
#   for row in matrix:
#     print(' '.join(map(str, row)))
matrix = []
count=0
# print("Enter the 5x5 matrix row by row (each row with 5 numbers separated by spaces):")

for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

found = False
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            current_row, current_col = i, j
            found = True
            break
    if found:
        break

center_row, center_col = 2, 2
steps = abs(current_row - center_row) + abs(current_col - center_col)
print(steps)