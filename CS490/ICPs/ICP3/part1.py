from pprint import pprint

def main(input):
    d = {}
    input_list = input.split()
    for word in input_list:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    pprint(d)
    

main("hello world this is my first hello")

