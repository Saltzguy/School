def get_sentence() -> list:
    sentence = input("Please inter your sentence -> ")
    return sentence.split()

def find_max(words: list)->str:
    sorted_words = sorted(words, key = len) # sorts the slist based on the length
    return sorted_words[-1]#returns the last item in the list

def find_middle(words:list) -> list:
    half = len(words) / 2 
    if len(words) % 2 == 0:
         #If the list has an even number of items
         return words[int(half) -1: int(half) +1]
    else:
        # if the list has an odd number of items
        return words[int(half)]
    return words

def reverse_words(words: list) -> str:
    #creates an empty string and reverse the words in place and adds it to the string
    #then returns the string
    sentence = ""
    for word in words:
        sentence = sentence + " " + word[::-1].lower()
    return sentence[1:]


lst = get_sentence()
print(find_middle(lst))
print(find_max(lst))
print(reverse_words(lst))
