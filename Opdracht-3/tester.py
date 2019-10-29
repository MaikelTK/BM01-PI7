from string import punctuation, digits
import re as re
from nltk.tokenize import RegexpTokenizer
import pandas as pd
import math


# Remove al chars except the alphabet
def clean_dataset(dataset):
    words = re.sub(r"\d+", "", dataset)  # Remove digits
    words = words.lower()
    tokenizer = RegexpTokenizer(r"\w+")  # Remove everything but words
    words = tokenizer.tokenize(words)  # Put words in list
    return words


def get_ngrams(n, text):
    ngram_list = []
    for word in text:
        for i in range(len(word)):
            ngram = (word[i:i+n])
            ngram_list.append(ngram)
    return ngram_list


def detect_language(n, text, csv):
    
    # Language scores
    languages = {'EN': [], 'DE': [],'FR': [],'ES': [],'IT': [],'AL': []}
    # Load bigram training set
    df = pd.read_csv(csv)
    
    print('Test data: ', text)
    text = clean_dataset(text) # Clean the test data
    print(len(text), 'words in test data.')
    input_ngrams = get_ngrams(n, text) # Create ngrams from test data
    print(len(input_ngrams), 'ngrams in test data')

    # For each ngrm in test data
    for ngram in input_ngrams:
        if ngram in df.values:
            index = (df.loc[df['ngram'] == ngram].index)[0]  # Locate row index
            row = df.loc[index] # Get row

            # For each language, find ngram chance
            for lan in languages:
                ngram_total = row[lan] # Get chance from row

                # Smoothing?
                if ngram_total == 0:
                    ngram_total = 1

                ngram_chance = (ngram_total / df[lan].sum()) # Normalize data
                languages[lan].append(math.log(ngram_chance)) # Save log(chance) in language list
    
    result = [-math.inf, '']
    for lan in languages:
        total = sum(languages[lan])
        if total > result[0]:
            result[0] = total
            result[1] = lan
        print(lan, total)
    print('Test data language = ', result[1])
        
    
                


text = 'el torro loco mucho grande'
tri_csv = 'trigram-bible.csv'
bi_csv = 'bigram-bible.csv'

detect_language(3, text, tri_csv)
