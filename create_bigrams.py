
#HAVEN'T DEBUGGED THIS

import nltk
import csv
import ipdb
import string
from gensim.models import Phrases
from gensim.models import Word2Vec
from gensim.utils import lemmatize
from gensim.parsing.preprocessing import STOPWORDS
from nltk.corpus import stopwords
from collections import Counter
import sys

"""
This module/script takes a list of (url, text) in csv form, and produces a list of bigrams
"""   

__author__ = "Ellie King"
__copyright__ = "Government Digital Service, 04/07/2017"

class UrlData:
    def __init__(self,url,text):
        self.url = url
        self.text = text

#fname = sys.argv[1]

def make_bigrams(fname):
    """Function that opens a csv list of urls, text and produce bigrams."""
    sentences = []
    bigram = Phrases()
    with open(fname,'r') as csvfile:
        urlreader = csv.reader(csvfile, delimiter=',')
        raw_documents = list(reader)

        print("Prepare documents")
        documents = [doc[2] for doc in raw_documents if doc[2] != '']
        

        for document in documents:
                raw_text = document.lower()
                tokens = lemmatize(raw_text, stopwords=STOPWORDS)
                sentences.append(tokens)
                bigram.add_vocab([tokens])
        
                return(bigram)

def bigrams_to_file(oname):
    """Function that writes data structure to (a .csv) file."""
    f = open(oname,'w')
    f.write('bigram\n')
    for row in bigram:
        f.write(row.bigram+'\n')
    f.close()
    return(0)

# executes only if run as a script and passed two arguments (input fileneame and output filename)
if __name__ == "__main__":
    bigram = make_bigrams(sys.argv[1])
    bigrams_to_file(sys.argv[2])

# example:
# python create_bigrams.py input/environment_urltext.csv input/environment_bigrams.csv


