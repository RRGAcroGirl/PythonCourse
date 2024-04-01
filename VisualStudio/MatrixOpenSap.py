# Write a program that lets the user input a two-dimensional matrix
# The program should first ask the user how many rows and columns
# Next, the program should ask the user for the elements of the matrix.
# Your program should read the values from the user row by row.
# Finally, the program should calculate and print the sums of the values in each row.

row = int(input("Please enter the number of rows:"))
column = int(input("Please enter the number of columns:"))

matrix = []
for r in range(row):
    matrix.append([])
    for c in range(column):
        ans = int(input("Please input an element for your matrix:"))
        matrix[r].append(ans)
print(matrix)

for r in range(row):
    sum_rows = 0 
    for num in matrix[r]:
        sum_rows += num
    print(sum_rows)
