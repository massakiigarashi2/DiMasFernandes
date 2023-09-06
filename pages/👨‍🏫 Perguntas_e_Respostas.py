import streamlit as st
import requests
import pandas as pd
from io import BytesIO

from PIL import Image #Lib para importação de imagem
import base64 #Lib para imagem de Background
import urllib3
from urllib3 import request

#import json
http = urllib3.PoolManager()

st.set_page_config(
    page_title="Perguntas&Respostas😀",
    page_icon="😀",
)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('fundo00.jpg')

rD1 = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vToT79VG5Elh9ywpqdaBPBNXtq7yTNnM_JnCuUJvib7LTDMnlrQCMrkYSQLKE9oK_z4x504ZUd88W5X/pub?gid=162224156&single=true&output=csv')
dataD = rD1.content
dfD = pd.read_csv(BytesIO(dataD), index_col=0)
dfD.columns = ['Mail', 'Pergunta', 'Palestrante', 'NomeMail']
NregD = len(dfD)

st.title(" ")
st.title(" ")
st.title("#👋 PERGUNTAS E RESPOSTAS")
st.sidebar.warning("Pergunte ao Palestrante")
form = st.form('Q&A')
PERGUNTA = form.text_input('Pergunta:') 
PALESTRANTE = form.text_input('Palestrante(s) a quem se destina:')
NOME_MAIL = form.text_input('Seu nome e e-mail:')     
link = 'https://docs.google.com/forms/d/e/1FAIpQLSer6EL-enkaAGqPIkxnSUfKamCUzGNswVwTVUsxP8-GzzPJVw/formResponse?&submit=Submit?usp=pp_url&entry.483600100='
link += str(PERGUNTA)
link += '&entry.1729513605='
link += str(PALESTRANTE)
link += '&entry.1163103571='
link += str(NOME_MAIL)
submit = form.form_submit_button('ENVIAR')
if submit:
    r = http.request('GET', link)
st.dataframe(dfD)
st.info("Desenv. por: Prof. Massaki Igarashi")
