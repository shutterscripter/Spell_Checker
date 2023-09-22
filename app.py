import streamlit as st
import pickle
from spello.model import SpellCorrectionModel

def correct(sentence):
    sp = SpellCorrectionModel(language = 'en')
    sp.load('/home/jay/Projects/Streamli/model.pkl')
    return sp.spell_correct(sentence)['spell_corrected_text']



chat = st.chat_input(placeholder="Enter the sentence")
if chat:
    with st.chat_message('ai'):
        st.write(chat)
        with st.spinner('Working on it...'):
            st.write("Corrected Sentence: ",correct(chat))

