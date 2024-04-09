# We are given two files: 1) key which has two numbers that detail the lentgh of a row and how many rows
# and 2) a bunch of symbols basically "." and "#"

# create some holding spaces to read the info from the file and put into w/ the detailed assignment criteria
grid_num = []
grid = []

#read the key file and get the 2 nummbers that will represent the column and row of a grid
#this will be put then "grid_num"
with open("key.txt", "r") as file2:
    for num in file2:
        grid_num.append(int(num))

#read the file with the symbols one charcter at a time and when the lenght of those chars reaches the row lenth
#a new line is created. this is all stored in "grid"
#and then the final statement is to go through each line in the grid and write it to the file
line = ""
with open("secret.txt", "r") as file:
    for char in file:
        line = line + char.strip()
        if len(line) == grid_num[0]:
            grid.append(line + "\n")
            line = ""

            with open("public.txt", "w") as file3:
                for pic in grid:
                    file3.write(pic)
