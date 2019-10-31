from nltk.tokenize import RegexpTokenizer
import re as re
from string import punctuation, digits
import numpy as np 
import csv
import math
import time


# Load file
def load_file(filepath:str):
    f = open(filepath, 'r')
    data = f.read()
    f.close()
    return data


# Save dictionary as json
def save_dict(dictionary: dict, filepath:str):
    f = open(filepath, 'w')
    f.write(str(dictionary))
    f.close()


# Remove al chars except the alphabet
def clean_dataset(dataset:list):
    words = re.sub(r"\d+", "", dataset)  # Remove digits
    words = words.lower()
    tokenizer = RegexpTokenizer(r"\w+")  # Remove everything but words
    words = tokenizer.tokenize(words)  # Put words in list
    return words


# Get Ngrams from text
def get_ngrams(text:list, n:int):
    text.sort()
    ngram_list = []

    for word in text:
        for i in range(len(word)):
            ngram = (word[i:i+n])
            ngram_list.append(ngram)
    ngram_list.sort()        
    return ngram_list


# Get Ngram frequencies
def get_ngram_freq(ngrams:list):
    unique_ngrams = np.array(ngrams)
    unique_ngrams = np.unique(unique_ngrams)
    
    ngram_dict = {}
    for ngram in unique_ngrams:
        ngram_dict.update({ngram:0})
    for ngram in ngrams:
        ngram_dict[ngram] += 1
    return ngram_dict


# Main methdo for 
def train_main(n:int):

     #Datasets
    languages = [
        ['DE', "Opdracht-3/traning_data/Bible_DE.txt"],  # German
        ['EN', "Opdracht-3/traning_data/Bible_EN.txt"],  # English
        ['FR', "Opdracht-3/traning_data/Bible_FR.txt"],  # French
        ['SP', "Opdracht-3/traning_data/Bible_ES.txt"],  # Spanish
        ['AL', "Opdracht-3/traning_data/Bible_AL.txt"],  # Albanian
        ['IT', "Opdracht-3/traning_data/Bible_IT.txt"]  # Italian
    ]

    all_lan_dict = {}

    for lan in languages:
        lan_id = lan[0]
        lan_url = lan[1]
        print('Training: ', lan_id)

        data = load_file(lan_url)
        data = clean_dataset(data)
        print(len(data), 'words')
        ngrams = get_ngrams(data, n)
        print(len(ngrams), 'ngrams')
        ngram_freq_dict = get_ngram_freq(ngrams)    
        all_lan_dict.update({lan_id: ngram_freq_dict})

    return all_lan_dict


'--------------------------------------------------'


# Calc ngram chances
def get_ngram_chances(text_ngrams:list, ngram_freq:dict):
    ngram_chances = []

    for ngram in text_ngrams:
        freq = 0        
        if ngram not in ngram_freq:
            freq = 1
        else:
            freq = ngram_freq[ngram]

        freqsum = sum(ngram_freq.values())
        chance = math.log(freq / freqsum)
        ngram_chances.append(chance)
    
    chance_score = sum(ngram_chances)
    return chance_score


# Get langauage with highest score
def get_highest_score(languages:dict):
    highest_score = max(languages.values())
    highest_score_language = ''

    for lan in languages:
        if languages[lan] == highest_score:
            highest_score_language = lan
    return [highest_score_language, highest_score]


# Test the given input text
def test_text(text:str, ngram_freq:dict, n:int):
    languages = {'EN': 0,'DE':0, 'FR':0, 'SP':0, 'AL':0, 'IT':0}
    start_time = time.time()
       

    text = clean_dataset(text)
    text_ngrams = get_ngrams(text, n)
    print(n, 'GRAMS: ')
    print(text_ngrams)

    for lan in languages:
        chance_score = get_ngram_chances(text_ngrams, ngram_freq[lan])
        languages[lan] = chance_score
        print(lan, ' log() score: ', chance_score)
    
    highest_score = get_highest_score(languages)
    print('Detected language: ', highest_score[0])
    duration = time.time() - start_time 
    print('Elapsed time: ', duration)


# Train bigram and trigram    
bigram_path = 'bigram.txt'
trigram_path = 'trigram.txt'

print('*' * 10,'Training bigrams', '*' * 10)
bigram_freq:dict = train_main(2)
print()
print('*' * 10, 'Training trigrams', '*' * 10)
trigram_freq:dict = train_main(3)

#save_dict(bigram_freq, bigram_path)
#save_dict(trigram_freq, trigram_path)
#bigram_freq = load_file(bigram_path)
#trigram_freq = load_file(trigram_path)

running = True
while running:
    print('*'*40)
    text = input('Feed me words... (or type quit to end):  b')
    if text == 'quit':
        running = False
    else:
        print('Bigram testing')
        test_text(text, bigram_freq, 2)
        print()
        print('Trigram testing')
        test_text(text, trigram_freq, 3)






