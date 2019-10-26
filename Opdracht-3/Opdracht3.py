from string import punctuation, digits, ascii_letters
import re as re
#from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
#from nltk.util import ngrams
import pandas as pd

data_url = 'Opdracht-3/traning_data/Bible-American_Standard_Version.txt'

columns = ['ngram', 'EN', 'DE', 'ES', 'FR', 'IT']

ngram_model = pd.DataFrame(columns=columns)

# Load dataset
def load_dataset(url):
    file = open(url, 'rt')
    data = file.read()
    file.close()

    print(len(data))

    #data = data[:1000000]
    return data

# Remove al chars except the alphabet
def clean_dataset(dataset):
    words = re.sub(r"\d+", "", dataset) # Remove digits
    words = words.lower()
    tokenizer = RegexpTokenizer(r"\w+") # Remove everything but words
    words = tokenizer.tokenize(words) # Put words in list
    
    return words

# Fill dataframe with ngrams
def create_ngram(text, n, language, df):
    text.sort()
    x = (len(text) / 10)
    counter = 0


    for word in text:
        counter += 1
        if counter >= x:
            print('+ 10%')
            counter = 0
        for i in range(len(word)):
            ngram = (word[i:i+n])
            if ngram in df.values:
                row = df.loc[df['ngram'] == ngram] #locate row of 
                df.loc[row.index, language] += 1
            else:
                df = df.append({'ngram': ngram, language : 1 }, ignore_index=True)
    print (df.sort_values(by=[language], ascending=False))
    return df

# Get dataset
dataset = load_dataset(data_url)
clean_data = clean_dataset(dataset)
#print(clean_data)
ngram_model = create_ngram(clean_data, 2, 'EN', ngram_model)
ngram_model.to_csv(r'export_bigram.csv', index=None, header=True)



