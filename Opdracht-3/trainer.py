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
    f = open(url, 'r')
    data = f.read()
    f.close()
    #data = data[200000:210000]
    return data


# Remove al chars except the alphabet
def clean_dataset(dataset):
    words = re.sub(r"\d+", "", dataset)  # Remove digits
    words = words.lower()
    tokenizer = RegexpTokenizer(r"\w+")  # Remove everything but words
    words = tokenizer.tokenize(words)  # Put words in list
    return words


# Get ngram frequencies from text
def create_ngram_freq(text, n, language, df):
    text.sort()
    x = (len(text) / 100)
    counter = 0
    percentage = 0
    print('Creating ', n, 'grams...')

    for word in text:

        counter += 1
        if counter >= x:
            percentage += 1
            print(percentage , '% Done...', round(x * percentage), '/', len(text))
            counter = 0

        for i in range(len(word)):
            ngram = (word[i:i+n])
            if ngram not in df.values: #smoothing by using 1 as default value instead of 0
                df = df.append({'ngram': ngram, 'EN': 1, 'DE': 1, 'ES': 1,
                                'FR': 1, 'IT': 1, 'AL': 1}, ignore_index=True)
            if ngram in df.values:
                row = df.loc[df['ngram'] == ngram]  # locate row of
                df.loc[row.index, language] += 1

    print(df.sort_values(by=[language], ascending=False))
    return df


# Create ngram chance df
def create_ngram_chance(freq_csv, chance_csv, lan):
    freq_df = pd.read_csv(freq_csv)
    chance_df = pd.read_csv(chance_csv)
    columns = lan 

    for index, row in freq_df.iterrows():
        ngram = row['ngram']
        ngram_chances = {'ngram': ngram, 'EN': 0, 'DE': 0, 'ES': 0, 'FR': 0, 'IT': 0, 'AL': 0}

        for col in columns:
            freq = row[col]
            chance = (freq / (freq_df[col].sum()))
            ngram_chances[col] = chance    

        chance_df = chance_df.append(ngram_chances, ignore_index=True)
    chance_df.to_csv(chance_csv, index=None, header=True) # Save dataframe as csv 


# Create Ngram dataframe
def train(n, csv):

    #Datasets
    languages = [
        ['DE', "Opdracht-3/traning_data/Bible_DE.txt"],  # German
        ['EN', "Opdracht-3/traning_data/Bible_EN.txt"],  # English
        ['FR', "Opdracht-3/traning_data/Bible_FR.txt"],  # French
        ['ES', "Opdracht-3/traning_data/Bible_ES.txt"],  # Spanish
        ['AL', "Opdracht-3/traning_data/Bible_AL.txt"],  # Albanian
        ['IT', "Opdracht-3/traning_data/Bible_IT.txt"]  # Italian
    ]

    # Create ngrams for each language 
    for lan in languages:
        df = pd.read_csv(csv)
        print(df)
        language = lan[0]
        text = lan[1]
        
        print('About to read: ', text)
        dataset = load_dataset(text)   # Load text dataset 
        print('Removing digits and punctuation')
        clean_data = clean_dataset(dataset)  # Clean the dataset
        print(len(clean_data), 'words found')

        ngram_model = create_ngram_freq(clean_data, n, language, df) # Get ngram dataframe from text
        print('Ngram dataframe: ', ngram_model)
        ngram_model.to_csv(csv, index=None, header=True) # Save dataframe as csv 


# Call all methods for training the model
def run_all():
    print('About to create BIgram frequency')
    train(2, bi_freq_csv)  
    print('About to create BIgram chances')
    create_ngram_chance(bi_freq_csv, bi_chance_csv, columns)

    print()
    print('About to create TRIgram frequency')
    train(3, tri_freq_csv)
    print('About to create Trigram chances')
    create_ngram_chance(tri_freq_csv, tri_chance_csv, columns)




tri_freq_csv = "Opdracht-3/csv/trigram-freq.csv"
tri_chance_csv = "Opdracht-3/csv/trigram-chance.csv"
bi_freq_csv = "Opdracht-3/csv/bigram-freq.csv"
bi_chance_csv = "Opdracht-3/csv/bigram-chance.csv"
columns = ['EN', 'DE', 'FR', 'ES', 'IT', 'AL' ]

create_empty_dataframe(tri_chance_csv) # Create empty csv
create_empty_dataframe(tri_freq_csv) # Create empty csv
create_empty_dataframe(bi_chance_csv) # Create empty csv
create_empty_dataframe(bi_freq_csv) # Create empty csv
run_all()