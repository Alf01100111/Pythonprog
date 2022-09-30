
def writing_file(data):
    with open('base.txt', 'a', encoding="utf-8") as file:
        file.write(f'{data}\n')

def read_file():
    with open('base.txt', 'r', encoding="utf-8") as file:
        temp = []
        data = file.read()
        data = data.split('\n')
        
        for i in range(len(data)):
            temp.append(data[i].split(','))
    return temp

def find_surname(surname,wherefind):
    for i in range(len(wherefind)):
        if surname in wherefind[i]:
            print(wherefind[i])

def del_elem(surname,wherefind):
    for i in range(len(wherefind)):
        if surname in wherefind[i]:
            wherefind.pop(i)
            break
    return wherefind
            


def writing_file_after_del(data):
    
    with open('base.txt', 'w', encoding="utf-8") as file:
        for row in data:
            file.write(','.join([str(elem) for elem in row])+'\n')




