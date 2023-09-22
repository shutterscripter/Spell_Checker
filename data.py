import pandas as pd
from spello.model import SpellCorrectionModel
import re

def correct(sentence):
    sp = SpellCorrectionModel(language = 'en')
    big = get_data()
    big_stripped = clean_data(big)
    sp.train(big_stripped)
    out = sp.spell_correct(sentence)
    sp.save('/home/jay/Projects/Streamli')
    return out['spell_corrected_text']



def get_data():
    with open("archive/big.txt","r") as f:
        big = f.readlines()
    big = [i.strip() for i in big]    
    return big

def clean_data(big):
    #Remove \t - tab
    big_t = [re.sub('\\t', ' ', text) for text in big]

    #Remove \\
    big_ = [re.sub("\\'", "", text) for text in big_t]

    #Remove
    big_r = [text for text in big_ if text != '']

    #Remove Special characters
    big_star = [re.sub(r'[^a-zA-Z]+', ' ', text) for text in big_r]

    #Remove leading and trailing spaces
    big_stripped = [text.strip() for text in big_star]
    return big_stripped

correct('jayesh')