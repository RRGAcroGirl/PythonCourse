# Creating a list of tuples for a txt file from a openSAP exercise
item_list = []
# read the text file make each item distinct on each line and add it to a list as a tuple
with open("invoice_data.txt", "r") as file:
    for item in file:
        line = item.split()
        tline = (line[0], int(line[1]), float(line[2]))
        item_list.append(tline)
# another for loop to read each item in our tupled list and print with specified beatified parameters
    for product in item_list:
        print(f"{product[0]:15s}{product[1]:3d}{product[2]:7.2f}{(product[1])*(product[2]):8.2f}")
