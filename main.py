import spacy

text = '''
... Dave watched as the forest burned up on the hill,
... only a few miles from his house. The car had
... been hastily packed and Marta was inside trying to round
... up the last of the pets. "Where could she be?" he wondered
... as he continued to wait for Marta to appear with the pets.
'''

nlp = spacy.load('en_core_web_sm')

doc = nlp(text)

token_list = [token for token in doc]

filtered_tokens = [token for token in doc if not token.is_stop]

lemmas = [
    f"token: {token}, lemma: {token.lemma_}"
    for token in filtered_tokens
]

filtered_tokens[1].vector

print(filtered_tokens[1].vector)