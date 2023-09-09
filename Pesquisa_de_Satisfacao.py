import streamlit as st
from PIL import Image #Lib para importação de imagem
import base64 #Lib para imagem de Background
import urllib3
from urllib3 import request
#import json

http = urllib3.PoolManager()

st.set_page_config(
    page_title="PesquisaSATISFACAO😀",
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

st.title(" ")
st.title(" ")
st.header("PESQUISA DE SATISFAÇÃO 😀 ")
st.sidebar.success("Pesquisa de Satisfação")
form = st.form('Pesquisa_de_Satisfação')
Option = st.radio('Sua opinião sobre este evento é: ',
                      ['um Elogio',
                       'uma Sugestão',
                       'uma Crítica'])
MSG = form.text_input('Em poucas palavras, resuma este evento:')    
link = 'https://docs.google.com/forms/d/e/1FAIpQLScSIJfNXVEfHe4ZZWu66gfDpmP5zPONWA86JD62cDsGSQsRnQ/formResponse?&submit=Submit?usp=pp_url&entry.1642074533='
link += str(Option)
link += '&entry.1002049217='
link += str(MSG)
submit = form.form_submit_button('✔️ ENVIAR')
if submit:
    r = http.request('GET', link)
st.info("Desenv. por: Prof. Massaki Igarashi")
