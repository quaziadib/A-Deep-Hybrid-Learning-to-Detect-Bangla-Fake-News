import re
import pandas as pd
from bnltk.stemmer import BanglaStemmer
from sklearn.utils import shuffle


df_aut = pd.read_csv('Authentic-48K.csv')
df_fak = pd.read_csv('Fake-1K.csv')
df = pd.concat([df_aut, df_fak], axis = 0)
df = df[['headline', 'content', 'label']]
df['space'] = " "
df['news'] = df['headline'] + df['space'] + df['content']
df = shuffle(df, random_state = 4)
df.reset_index(inplace=True, drop=True)


def cleanpunc(sentence):
    cleaned = re.sub(r'[?|!|\'|"|#|%|@|<|>]',r'', sentence)
    cleaned = re.sub(r'[.|,|)|(|\|/|।|”|“|’|‘]', r' ', cleaned)
    return cleaned

stop = []
with open('stopword.txt', 'r', encoding="utf8") as file:
    for row in file: 
        row = row.replace("\n", "")
        stop.append(row)



bn_stemmer = BanglaStemmer()
i = 0
strl = ' '
final_string = []
s = ''
for sent in df['news'].values:
    filtered_sentence = []
    for w in sent.split():
        for cleaned_words in cleanpunc(w).split():
            if len(cleaned_words) > 2:
                if cleaned_words not in stop:
                    s = bn_stemmer.stem(cleaned_words)
                    filtered_sentence.append(s)
                else:
                    continue
            else:
                continue
    str1 = " ".join(filtered_sentence)
    final_string.append(str1)
    i+=1
    
df['cleaned'] = final_string

df.to_csv('preprocessed.csv', index=False)
