list_of_words = []
with open('input.txt', 'r') as i:
    for line in i:
        list_of_words.append(line[:-1])
    i.close()


with open('output.txt', 'w') as o:
    for word in list_of_words:
        o.write(word +" "+ str(len(word)) + '\n')
    o.close()
   
