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


# Get ngrams from given text
def get_ngrams(n, text):
    ngram_list = []
    for word in text:
        for i in range(len(word)):
            ngram = (word[i:i+n])
            ngram_list.append(ngram)
    return ngram_list


# Get ngram chances from given text
def get_chances(n, text, csv):
    # Language scores
    languages = {'EN': [], 'DE': [],'FR': [],'ES': [],'IT': [],'AL': []}
    # Load bigram training set
    df = pd.read_csv(csv)
    
    input_ngrams = get_ngrams(n, text) # Create ngrams from test data
    print(len(input_ngrams), 'ngrams in test data')

    # For each ngrm in test data
    for ngram in input_ngrams:
        if ngram in df.values:
            index = (df.loc[df['ngram'] == ngram].index)[0]  # Locate row index
            row = df.loc[index] # Get row

            # For each language, find ngram chance
            for lan in languages:
                ngram_chance = row[lan] # Get chance from row
                languages[lan].append(math.log(ngram_chance)) # Save log(chance) in language list

    return languages


# Get the correct languages based on ngram chances
def get_language(languages):
    result = [-math.inf, '']
    for lan in languages:
        total = sum(languages[lan])
        if total > result[0]:
            result[0] = total
            result[1] = lan
        print(lan, total)
    print('Test data language = ', result[1])


# Run all methods for detecting a language
def test():
    tri_chance_csv = "Opdracht-3/csv/trigram-chance.csv"
    bi_chance_csv = "Opdracht-3/csv/bigram-chance.csv"

    text = input('Feed me words... ')
    text = clean_dataset(text) # Clean the test data
    print(len(text), ' total words in test text.')
    print(text)
    print('About to check the language with bigrams.')
    languages = get_chances(2, text, bi_chance_csv)
    get_language(languages)
    print('About to check the language with trigrams.')
    languages = get_chances(3, text, tri_chance_csv)
    get_language(languages)

# Run file
test()
