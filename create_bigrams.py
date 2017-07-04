import nltk
import csv
# import ipdb
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

Example usage:
python create_bigrams.py input/test_urltext.csv input/test_bigrams.csv
"""   

__author__ = "Ellie King and Nicky Zachariou (reviewer)"
__copyright__ = "Government Digital Service, 04/07/2017"


def make_bigrams(fname):
    """Function that opens a csv list of urls, text and produce bigrams."""
    sentences = []
    bigram = Phrases()
    with open(fname,'r') as csvfile:
        urlreader = csv.reader(csvfile, delimiter=',')
        raw_documents = list(urlreader)

        # print("Prepare documents")
        documents = [doc[1] for doc in raw_documents if doc[1] != '']

        for document in documents:
            raw_text = document.lower()
            tokens = lemmatize(raw_text, stopwords=STOPWORDS)
            sentences.append(tokens)
            bigram.add_vocab([tokens])
    # print dir(bigram.vocab)  
    return(bigram)

def bigrams_to_file(oname):
    """Function that writes data structure to (a .csv) file."""
    f = open(oname,'w')
    f.write('bigram\n')
    for row in bigram.vocab:
        # print row
        f.write(row+'\n')
    f.close()
    return(0)

# executes only if run as a script and passed two arguments (input fileneame and output filename)
if __name__ == "__main__":
    bigram = make_bigrams(sys.argv[1])
    bigrams_to_file(sys.argv[2])
