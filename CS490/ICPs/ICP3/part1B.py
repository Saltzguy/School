

def main(input):
    input = input.lower()
    a = 0
    v = {'a','e','i','o','u'}
    for c in input:
        if c in v:
            a = a + 1

    print("Count of vowels is " + str(a))



main("Python Prograaaaaam")
main("aeiou")
main("cccccc")
main("aaaaaaa")