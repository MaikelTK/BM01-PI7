import pandas as pd
from string import punctuation, digits
import re as re
from nltk.tokenize import RegexpTokenizer


# Create new (empty dataframe)
def create_empty_dataframe(csv):
    columns = ['ngram', 'EN', 'DE', 'ES', 'FR', 'IT', 'AL']
    df = pd.DataFrame(columns=columns)
    df.to_csv(csv, index=None, header=True)

# Load dataset
def load_dataset(url):
    file = open(url, 'rt')
    data = file.read()
    file.close()
    limit = 200000

    data = data[limit:(limit * 2)]
    return data

# Remove al chars except the alphabet
def clean_dataset(dataset):
    words = re.sub(r"\d+", "", dataset)  # Remove digits
    words = words.lower()
    tokenizer = RegexpTokenizer(r"\w+")  # Remove everything but words
    words = tokenizer.tokenize(words)  # Put words in list
    return words


# Fill dataframe with ngrams
def create_ngram(text, n, language, df):
    text.sort()
    x = (len(text) / 10)
    counter = 0
    percentage = 0
    print('Creating ', n, 'grams...')

    for word in text:

        counter += 1
        if counter >= x:
            percentage += 1
            print((percentage * 10), '% Done...')
            counter = 0

        for i in range(len(word)):
            ngram = (word[i:i+n])
            if ngram not in df.values:
                df = df.append({'ngram': ngram, 'EN': 0, 'DE': 0, 'ES': 0,
                                'FR': 0, 'IT': 0, 'AL': 0}, ignore_index=True)
            if ngram in df.values:
                row = df.loc[df['ngram'] == ngram]  # locate row of
                df.loc[row.index, language] += 1

    print(df.sort_values(by=[language], ascending=False))
    return df


# Create Ngram dataframe
def main(n, csv):

    #Datasets
    languages = [
        ['DE', 'Opdracht-3/traning_data/Bible_DE.txt'],  # German
        ['EN', 'Opdracht-3/traning_data/Bible_EN.txt'],  # English
        ['FR', 'Opdracht-3/traning_data/Bible_FR.txt'],  # French
        ['ES', 'Opdracht-3/traning_data/Bible_ES.txt'],  # Spanish
        ['AL', 'Opdracht-3/traning_data/Bible_AL.txt'],  # Albanian
        ['IT', 'Opdracht-3/traning_data/Bible_IT.txt']  # Italian
    ]

    df = pd.read_csv(csv)
    print(df)
    print('0:Duits | 1:Engels | 2:Frans | 3:Spaans | 4:Albanees | 5:Italiaans')
    number = input('Select language 0-5: ')
    num = int(number)
    language = languages[num]
    lan = language[0]
    text = language[1]

    print('Read file: ', text)
    dataset = load_dataset(text)   # Load text dataset
 
    print('Removing digits and punctuation')
    clean_data = clean_dataset(dataset)  # Clean the dataset
    print(len(clean_data), 'words found')

    ngram_model = create_ngram(clean_data, n, lan, df) # Get ngram dataframe from text
    print('Ngram dataframe: ', ngram_model)
    ngram_model.to_csv(csv, index=None, header=True) # Save dataframe as csv


tri_csv = 'trigram-bible.csv'
bi_csv = 'bigram-bible.csv'

#create_empty_dataframe()
main(3, tri_csv)
#main(2, bi_csv)