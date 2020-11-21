import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import requests

df = pd.read_csv('wikilinks.csv', header=None)

def get_link():
    return(df.sample().iloc[0][0])

def get_title(link):
    req = requests.get(link)
    soup = BeautifulSoup(req.content, 'html.parser')
    return(soup.find('h1').get_text())

st.title("Looking for an interesting or weird article from Wikipedia?")
if st.button("Yep!"):
    url = str(get_link())

    link = '['+ get_title(url) +'](' + url + ')'
    st.markdown(link, unsafe_allow_html=True)
