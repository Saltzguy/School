import urllib.request
import os
from pprint import pprint
import string
from nltk import wordpunct_tokenize, pos_tag, ne_chunk, word_tokenize,PorterStemmer,LancasterStemmer,SnowballStemmer
from nltk.util import trigrams
import re


from nltk.stem import PorterStemmer, WordNetLemmatizer

from bs4 import BeautifulSoup

printable = set(string.printable)

def save_data_from_webpage():
    fname = "input.txt"
    #checks to see if the output file exizts
    file_exist = os.path.isfile(fname)
    
    if not file_exist:
        req = urllib.request.Request("https://en.wikipedia.org/wiki/Python_(programming_language)")
        res = urllib.request.urlopen(req)

        #the entire webpage with html tags
        soup = BeautifulSoup(res, "html.parser")

        #removes the html tags from the webpage
        text = soup.get_text()
        
        with open(fname, 'w') as file:
            #removes special char and numbers
            text = re.sub('[^ a-zA-Z]',' ', text) 
            file.write(text)
            file.close()

def get_data_from_file() -> str:
    #opens the files and returns the text
    fname = "input.txt"
    with open(fname, 'r') as file:
        text = file.read()
    return text

def main():
    save_data_from_webpage()
    
    text = get_data_from_file()
  
    
    #creates a list of the tolkenized words
    tt = word_tokenize(text)
    pprint(tt)

    #creates a new list for the steam words using all of the stemmers
    psteam = PorterStemmer()
    psteam_list = []
    for word in tt:
        psteam_list.append(psteam.stem(word))
    pprint(psteam_list)

    lsteam = LancasterStemmer()
    lsteam_list = []
    for word in tt:
       lsteam_list.append(lsteam.stem(word))
    pprint(lsteam_list)

    ssteam = SnowballStemmer()
    ssteam_list = []
    for word in tt:
        ssteam_list.append(ssteam.stem(word))
    pprint(ssteam_list)

    p = set(psteam_list)
    l = set(lsteam_list)
    s = set(ssteam_list)
    #displays the different steams
    pprint(s.difference(l.difference(p)))

    #pos taging
    pos_list = pos_tag(text)
    pprint(pos_list)

    #creates a new list for the lematized words
    lemmatizer = WordNetLemmatizer()
    lem = []
    for word in tt:
        lem.append(lemmatizer.lemmatize(word)) 
    #pprint(lem)
    
    # returns a generator of trigrams using the tokenized list tt
    trig = trigrams(tt)
    displays the results
    print(list(trig))
    
    #ne_chunck finds non overlapping groups
    #pos_tag ids how the text is used in speech
    NamedEntity = ne_chunk(pos_tag(wordpunct_tokenize(text)))
    print(NamedEntity)
    

main()
