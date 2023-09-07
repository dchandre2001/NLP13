##Assignment No.01##
#Name:Dipali Chandre 
##Roll No:13
#Batch:B1
#Title:"Text Pre-Processing using NLP operations:perform Tokenization
# Stop word removal,Lemmatization ,Part-of-Speech Tagging use any sample text"

#import Libraries
import spacy
#language model loaded
nlp = spacy.load("en_core_web_sm")
about_text = (
   "The man who does not read books has no advantage over the one who cannot read them."
    "Teachers can open the door,but you must enter it yourself."
)
##1-------Tokenization---------##

about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)


##2-------Stop Words-----------###

about_doc = nlp(about_text)
print([token for token in about_doc if not token.is_stop])


##3-------Lemmatization-----------##

about_doc=nlp(about_text)
for token in about_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20}:{str(token.lemma_)}")
        

 ##4-------Part of Speech----------##   
               
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )
 
 ##------------------OUTPUT---------------##
# """ The 0
# man 4
# who 8
# does 12
# not 17
# read 21
# books 26
# has 32
# no 36
# advantage 39
# over 49
# the 54
# one 58
# who 62
# can 66
# not 69
# read 73
# them 78
# . 82
# Teachers 83
# can 92
# open 96
# the 101
# door 105
# , 109
# but 110
# you 114
# must 118
# enter 123
# it 129
# yourself 132
# . 140
# [man, read, books, advantage, read, ., Teachers, open, door, ,, enter, .]
#                  The : the
#                 does : do
#                books : book
#                  has : have
#                 them : they
#             Teachers : teacher

# TOKEN: The
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: man
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: who
# =====
# TAG: WP         POS: PRON
# EXPLANATION: wh-pronoun, personal

# TOKEN: does
# =====
# TAG: VBZ        POS: AUX
# EXPLANATION: verb, 3rd person singular present

# TOKEN: not
# =====
# TAG: RB         POS: PART
# EXPLANATION: adverb

# TOKEN: read
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: books
# =====
# TAG: NNS        POS: NOUN
# EXPLANATION: noun, plural

# TOKEN: has
# =====
# TAG: VBZ        POS: VERB
# EXPLANATION: verb, 3rd person singular present

# TOKEN: no
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: advantage
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: over
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: the
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: one
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: who
# =====
# TAG: WP         POS: PRON
# EXPLANATION: wh-pronoun, personal

# TOKEN: can
# =====
# TAG: MD         POS: AUX
# EXPLANATION: verb, modal auxiliary

# TOKEN: not
# =====
# TAG: RB         POS: PART
# EXPLANATION: adverb

# TOKEN: read
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: them
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

# TOKEN: Teachers
# =====
# TAG: NNS        POS: NOUN
# EXPLANATION: noun, plural

# TOKEN: can
# =====
# TAG: MD         POS: AUX
# EXPLANATION: verb, modal auxiliary

# TOKEN: open
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: the
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: door
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: ,
# =====
# TAG: ,          POS: PUNCT
# EXPLANATION: punctuation mark, comma

# TOKEN: but
# =====
# TAG: CC         POS: CCONJ
# EXPLANATION: conjunction, coordinating

# TOKEN: you
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: must
# =====
# TAG: MD         POS: AUX
# EXPLANATION: verb, modal auxiliary

# TOKEN: enter
# =====
# TAG: VB         POS: VERB
# EXPLANATION: verb, base form

# TOKEN: it
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: yourself
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer  """