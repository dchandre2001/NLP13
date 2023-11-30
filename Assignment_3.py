"""
Assignment no 3:
Name:Chandre Dipali Ravindre
Batch:B1
Roll no: 13
Title: "Assignment Based on NER."
"""
import spacy
NER = spacy.load("en_core_web_sm")
raw_text="""raw_text="The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."""
text1= NER(raw_text)
for word in text1.ents:
    print(word.text,word.label_)

"""
OUTPUT:
Indian Space Research Organisation ORG
India GPE
Bengaluru GPE
Department of Space ORG
India GPE
ISRO ORG
DOS ORG
"""