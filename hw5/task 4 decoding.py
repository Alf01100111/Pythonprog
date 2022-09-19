
with open('task 4 string.txt', 'r') as data:
    
    my_str = data.read()

string = list(my_str)

for j in range(0,len(string),2):
    i = 0
    while i <= int(string[j]):

        print(string[j+1], end='') 
        i += 1