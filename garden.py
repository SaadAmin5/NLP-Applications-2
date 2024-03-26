#importing spacy package
import spacy
nlp=spacy.load('en_core_web_sm')   #loading small english language model


# made a list of garden path sentences and assigned it to a variable gardenpathsentences
gardenpathSentences=['The sour drink from the ocean.', 'The man who whistles tunes pianos.',
                     'We painted the wall with cracks.', 'The raft floated down the river sank.']
print('List of garden-path sentence is: ', gardenpathSentences)
print('\n')


#now adding additional 3 sentences to previous list, I used extend function for that purpose as the sentences were more than one.
gardenpathSentences.extend(['Mary gave the child a Band-Aid.', 
                            'That Jill is never here hurts.',
                            'The cotton clothing is made of grows in Mississippi.'])

print('Updated list of garden-path sentence is:', gardenpathSentences)
print('\n')


# Tokenizing each sentence in the list, and performing named entity recognition.
for sentence in gardenpathSentences:
    nlp_sentence=nlp(sentence)       #processing the text usig nlp
    
    for token in nlp_sentence.ents:    #creating token (tokenization) and performing Named Entity Recognition (NER)
        print('Entity: ',token.text, ',','Label: ', token.label_, ',', token.label)

print('\n')


#printing the meaning of entities i don't understand
print('Meaning of PERSON: ', spacy.explain('PERSON') )
print('Meaning of GPE: ', spacy.explain('GPE'))


'''
Questions:
a) What was the entity and its explanation that you looked up?
b) Did the entity make sense in terms of the word associated with it?


For PERSON (spacy.explain('PERSON') :
a) I looked up for PERSON label, the entity for it was Mary. Its explanination came out to be People, including fictional.
b) Yes, the entity made sense in terms of word associated with it. 

For GPE (spacy.explain('GPE')):
a) I looked up for GPE label, the entity for it was Mississippi. Its explaination came out to be Countries, cities, states. 
b) Yes, the entity made sense in terms of word associated with it.  '''
