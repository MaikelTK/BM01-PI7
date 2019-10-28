from string import punctuation, digits
import re as re
from nltk.tokenize import RegexpTokenizer
import pandas as pd

# Load dataset


def load_dataset(url):
    file = open(url, 'rt')
    data = file.read()
    file.close()
    limit = len(data)

    print('Read file: ', url)
    print('File len: ', len(data))
    print('Using: ', limit, '/', len(data))
    #data = data[limit:(limit * 2)]

    return data

# Remove al chars except the alphabet


def clean_dataset(dataset):
    words = re.sub(r"\d+", "", dataset)  # Remove digits
    words = words.lower()
    tokenizer = RegexpTokenizer(r"\w+")  # Remove everything but words
    words = tokenizer.tokenize(words)  # Put words in list
    print('Removing digits and punctuation')
    print(len(words), 'words found')
    return words

# Fill dataframe with ngrams


def create_ngram(text, n, language, df):
    text.sort()
    x = (len(text) / 10)
    counter = 0
    percentage = 0
    print('Creating bigrams...')

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
                                'FR': 0, 'IT': 0, 'PO': 0}, ignore_index=True)
            if ngram in df.values:
                row = df.loc[df['ngram'] == ngram]  # locate row of
                df.loc[row.index, language] += 1

    print(df.sort_values(by=[language], ascending=False))
    return df


def create_empty_dataframe():
    columns = ['ngram', 'EN', 'DE', 'ES', 'FR', 'IT', 'PO']
    df = pd.DataFrame(columns=columns)
    df.to_csv(r'export_bigram-Bible.csv', index=None, header=True)


def main(url, language, dataframe):
    # Load text dataset
    dataset = load_dataset(url)

    # Clean the dataset
    clean_data = clean_dataset(dataset)

    # Get ngram dataframe from text
    ngram_model = create_ngram(clean_data, 2, language, dataframe)

    print('Ngram dataframe: ', ngram_model)

    # Save dataframe as csv
    ngram_model.to_csv(r'export_bigram-Bible.csv', index=None, header=True)

# ----------------------------------------------------------------------------- #


def create_ngram_model():

    languages = [
        ['DE', 'Opdracht-3/traning_data/Bible_DE.txt'],  # German
        ['EN', 'Opdracht-3/traning_data/Bible_EN.txt'],  # English
        ['FR', 'Opdracht-3/traning_data/Bible_FR.txt'],  # French
        ['ES', 'Opdracht-3/traning_data/Bible_ES.txt'],  # Spanish
        ['PO', 'Opdracht-3/traning_data/Bible_PO.txt'],  # Portuguese
        ['IT', 'Opdracht-3/traning_data/Bible_IT.txt']  # Italian
    ]

    df = pd.read_csv('export_bigram-Bible.csv')
    print(df)

    print('0:DE | 1:EN | 2:FR | 3:ES | 4:PO | 5:IT')
    number = input('Select language 0-5: ')
    num = int(number)
    language = languages[num]
    lan = language[0]
    text = language[1]

    main(text, lan, df)


def detect_language(n):
    columns = ['EN', 'DE', 'ES', 'FR', 'IT', 'PO']
    points = [0, 0, 0, 0, 0, 0]
    df = pd.read_csv('export_bigram-Bible.csv')

    text = 'Ich habe keine Ahnung, was ich tue. Ich habe keine Ich habe keine Ich habe keine Ahnung, was ich tue. Ich habe keine Ich habe keine '
    text = clean_dataset(text)
    input_ngram = []

    # Create ngram model for input text
    for word in text:
        for i in range(len(word)):
            ngram = (word[i:i+n])
            input_ngram.append(ngram)

    for col in columns:
        print(col)
        lan_ods = []

        for ngram in input_ngram:

            if ngram in df.values:
                row = (df.loc[df['ngram'] == ngram].index)  # locate row
                index = row[0]
                row = df.loc[index]
                ngram_total = row[col]
                # Normalize ngram for language
                ngram_chance = (ngram_total / df[col].sum())

            else:
                ngram_chance = 1
                # ngram chance = 1
                # kans * kans * kans / som van kansen
                # Fill ngram model for input text
            lan_ods.append(ngram_chance)
        # print(lan_ods)
        som = (sum(lan_ods))

        # Calc odds for lang
        result = 1
        for x in lan_ods:
            result = (result * x)

        print(som)

        # print(ngram_chance)
        #index = columns.index(col)
        #points[index] += ngram_chance


detect_language(2)


# create_empty_dataframe()
# create_ngram_model()
