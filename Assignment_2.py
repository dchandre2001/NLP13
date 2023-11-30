#Name:Dipali Ravindra Chandre
#Roll No:13
import gensim
from gensim import corpora
from gensim.models.word2vec import Word2Vec
from multiprocessing import cpu_count
import gensim.downloader as api
from gensim.utils import simple_preprocess
import numpy as np
from pydantic import model_serializer, model_validator
#Bag-Of-Word
text1 = ["""Gensim is a free open-source Python library for representing documents as semantic vectors,
           as efficiently and painlessly as possible. Gensim is designed 
           to process raw, unstructured digital texts using unsupervised machine learning algorithms."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)
g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)

#TF-IDF
text = ["The food is excellent but the service can be better",
        "The food is always delicious and loved the service",
        "The food was mediocre and the service was terrible"]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = model.TfidfModel(g_bow, smartirs='ntc')

print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])
    

#Wordtovec
dataset = api.load("text8")
words = [d for d in dataset]

data1 = words[:1000]
w2v_model = Word2Vec(data1, min_count = 0, workers=cpu_count())

#OUTPUT

# The dictionary has: 29 tokens

# {'Gensim': 0, 'Python': 1, 'a': 2, 'algorithms.': 3, 'and': 4, 'as': 5, 'designed': 6, 'digital': 7, 'documents': 8, 'efficiently': 9, 'for': 10, 'free': 11, 'is': 12, 'learning': 13, 'library': 14, 'machine': 15, 'open-source': 16, 'painlessly': 17, 'possible.': 18, 'process': 19, 'raw,': 20, 'representing': 21, 'semantic': 22, 'texts': 23, 'to': 24, 'unstructured': 25, 'unsupervised': 26, 'using': 27, 'vectors,': 28}
# Bag of Words :  [[(0, 2), (1, 1), (2, 1), (3, 1), (4, 1), (5, 3), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 2), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1), (26, 1), (27, 1), (28, 1)]]
# Dictionary : 
# [['be', 1], ['better', 1], ['but', 1], ['can', 1], ['excellent', 1], ['food', 1], ['is', 1], ['service', 1], ['the', 2]]
# [['food', 1], ['is', 1], ['service', 1], ['the', 2], ['always', 1], ['and', 1], ['delicious', 1], ['loved', 1]]
# [['food', 1], ['service', 1], ['the', 2], ['and', 1], ['mediocre', 1], ['terrible', 1], ['was', 2]]
# TF-IDF Vector:
# [['be', 0.44], ['better', 0.44], ['but', 0.44], ['can', 0.44], ['excellent', 0.44], ['is', 0.16]] [['is', 0.2], ['always', 0.55], ['and', 0.2], ['delicious', 0.55], ['loved', 0.55]] [['and', 0.15], ['mediocre', 0.4], ['terrible', 0.4], ['was', 0.81]]
