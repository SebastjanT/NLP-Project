import codecs
import afinn
import json
import matplotlib.pyplot as plt
import sklearn
import numpy as np
import pandas as pd
import spacy
import os
import pathlib
import nltk

with codecs.open('1-1000.txt') as f:
    file = f.read()
    file = file.split("\n")

common_words = set(file)

datadir1 = pathlib.Path(os.getcwd()) / '../data/imapbook'
datadir2 = pathlib.Path(os.getcwd()) / '../data/gutenberg'
nlp = spacy.load('en_core_web_lg')
# nltk.download('punkt') # se požene enkrat in je ok


def process_ner(input_tokenized):

    out = []

    af = afinn.Afinn()
    sentiment = [af.score(x) for x in input_tokenized]
    alignment = np.sum(sentiment) / len(np.nonzero(sentiment)[0]) * -2

    for t in input_tokenized:

        cur = nlp(t)

        name_list = [x for x in cur.ents if x.label_ in ['PERSON']]
        name_list = [str(x).lower().replace("'s", "") for x in name_list]
        name_list = [x.split(' ') for x in name_list]
        name_list = process_list(name_list)
        name_list = [x for x in name_list if len(x) >= 2]
        # name_list = [x for x in name_list if x not in common_words]

        if name_list != []:
            out.append(name_list)

    out = process_list(out)
    import collections
    out = collections.Counter(out)
    out = [x for x in out if out[x] >= 0.0005 * len(input_tokenized)]

    return out, alignment


def read(story, path):

    stories = os.listdir(path)
    stories = [i for i in stories if i.find(story) >= 0]
    novel = ''
    for s in stories:
        with codecs.open(path / s, 'r', encoding='utf-8') as f:
            data = f.read().replace('\r', ' ').replace('\n', ' ').replace("\'", "'")
        novel += ' ' + data

    return novel


# def flatten(l):
#     try:
#         return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]
#     except IndexError:
#         return []


def process_list(oldlist):
    newlist = []
    for l in oldlist:
        if type(l) == list:
            newlist += process_list(l)
        else:
            newlist += [l]

    return newlist


def top_names(name_list, novel):

    vect = sklearn.feature_extraction.text.CountVectorizer(vocabulary=name_list, stop_words='english')
    name_frequency = vect.fit_transform([novel.lower()])
    name_frequency = pd.DataFrame(name_frequency.toarray(), columns=vect.get_feature_names_out())
    name_frequency = name_frequency.T
    name_frequency = name_frequency.sort_values(by=0, ascending=False)
    name_frequency = name_frequency[0:10]
    names = list(name_frequency.index)
    name_frequency = list(name_frequency[0])

    return names, name_frequency


if __name__ == '__main__':

    # curstory = 'Doyle_AStudyinScarlet'

    short_stories = []

    for file in os.listdir(datadir2):
        if file.endswith('.txt'):
            short_stories.append(file)

    # for file in os.listdir(datadir2):
    #     if file.endswith('.txt'):
    #         short_stories.append(file)

    for curstory in short_stories:

        print('delam na ' + curstory)

        story = read(curstory, datadir2)

        sent_tokens = nltk.sent_tokenize(story)

        out_ner, alignment = process_ner(sent_tokens)

        chars, freqs = top_names(out_ner, story)

        with open(f"{curstory}.txt", "w") as output:
            output.write(str(chars))
            output.write(str(freqs))

    print('done')





