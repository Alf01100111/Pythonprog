# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('task1abv.txt', 'r') as data:
    
    my_str = data.read()

print (' '.join(filter(lambda x: not 'abc' in x, my_str.split())))

# какая то ерунда с кодировкой, русский текст превращается в белиберду, поэтому работаю с анг.