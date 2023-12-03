from utils import get_valid_neighbors, cache, int_list

file=open("i.txt","r")
rows = file.read().split("\n")
for i in range(len(rows)):
    print(rows[i])
