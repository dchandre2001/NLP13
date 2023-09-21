#Assignment No.02##
#Name:Dipali Chandre 
##Roll No:13
#Batch:B1
#Title:"Assignment based on bag of words"


import gensim
from gensim import corpora
text1 = ["The food is excellent but the service can be better",
        "The food is always delicious and loved the service",
        "The food was mediocre and the service was terrible"]
tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)
# Creating Bag Of Words
g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)

# Creating TF-IDF
print("Dictionary : ")
for item in g_bow:
    print([[g_dict1[id], freq] for id, freq in item])


"""OUTPUT"""
# Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)], [(0, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1)], [(0, 1), (6, 1), (8, 1), (9, 1), (11, 1), (14, 1), (15, 1), (16, 2)]]
# Dictionary : 
# [['The', 1], ['be', 1], ['better', 1], ['but', 1], ['can', 1], ['excellent', 1], ['food', 1], ['is', 1], ['service', 1], ['the', 1]]
# [['The', 1], ['food', 1], ['is', 1], ['service', 1], ['the', 1], ['always', 1], ['and', 1], ['delicious', 1], ['loved', 1]]
# [['The', 1], ['food', 1], ['service', 1], ['the', 1], ['and', 1], ['mediocre', 1], ['terrible', 1], ['was', 2]]