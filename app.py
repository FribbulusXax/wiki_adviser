import streamlit as st
import pandas as pd
import webbrowser

df = pd.read_csv('wikilinks.csv', header=None)

def get_link():
    return(df.sample().iloc[0][0])

st.title("Looking for an interesting or weird article from Wikipedia?")
if st.button("Yep!"):
    webbrowser.open_new_tab(str(get_link()))