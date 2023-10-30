uniwords = set()

with open("romeo.txt", "r") as file:
    
    for line in file:
        words = line.split()
        uniwords.update(words)

uniwords_list = sorted(uniwords) 

print(uniwords_list)
