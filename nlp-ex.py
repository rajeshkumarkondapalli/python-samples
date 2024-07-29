import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

def extract_entities_and_relationships(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    relations = []
    
    for token in doc:
        if token.dep_ in ('nsubj', 'dobj'):
            subject = token.head.text
            object_ = token.text
            relations.append((subject, token.dep_, object_))
    
    return entities, relations

text = "I am looking at buying building startup worth $1 billion" # test input
entities, relations = extract_entities_and_relationships(text)
print("Entities:", entities)
print("Relations:", relations)
