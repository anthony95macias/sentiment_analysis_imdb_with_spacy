import os
import random 
import spacy

def load_training_data(
    data_directory: str = "aclImdb/train`",
    split: float = 0.8,
    limit:  int = 0, 
) -> tuple:
    
# LOAD FROM THE FILE:
    reviews = []
    for label in ["pos", "neg"]:
        labelded_diretory = f"{data_directory}/{label}"
        for review in os.listdir(labelded_diretory):
            if review.endswith(".txt"):
                with open(f"{labelded_diretory}/{review}") as f:
                    text = f.read()
                    text = text.replace("<br />", "\n","\n")
                    if text.strip():
                        spacy_label = {
                            "cats": {
                                "pos": "pos" == label,
                                "neg": "neg" == label 
                            }
                        }
                        reviews.append((text,spacy_label))
    random.shuffle(reviews)
    
    if limit:
        reviews = reviews[:limit]
    split = int(len(reviews) * split)
    return reviews[:split], reviews[split:]
