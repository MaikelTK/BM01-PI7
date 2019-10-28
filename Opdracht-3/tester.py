from string import punctuation, digits
import re as re
from nltk.tokenize import RegexpTokenizer
import pandas as pd


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
    
    text = clean_dataset(text) # Clean the test data
    input_ngrams = get_ngrams(n, text) # Create ngrams from test data

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
                languages[lan].append(ngram_chance) # Save chance in language list
    
    # TODO: calculate percentage
    # kans * kans * kans / som van kansen
    test_lan = ''
    test_val = 0    
    for lan in languages:
        total = sum(languages[lan])
        print(lan, total)

        if total > test_val:
            test_val = total
            test_lan = lan
    
    print('Language = ', test_lan)
    
                


text = 'Unë shes makinën time blu te gjyshi sepse jam i varur nga demi i kuq dhe kafeja dhe ëmbëlsirat.'
tri_csv = 'trigram-bible.csv'
bi_csv = 'bigram-bible.csv'

detect_language(3, text, tri_csv)
