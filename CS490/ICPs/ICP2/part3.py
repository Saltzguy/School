list_of_list = []
with open('input-part3', 'r') as i:
    for line in i:
        list_of_list.append(list(line.split()))
    i.close()

for lst in list_of_list:
    s = ""
    for l in lst:
        s = s + l
    print(s +" " +str(len(lst)))
