import streamlit as st
import openai
from streamlit_chat import message
from PIL import Image # Lib para carregar imagem no Streamlit
from gtts import gTTS #Lib para Conversão Text2Voice. Em seguida pode usar OpenAI para converter voice para texto
import os
  
col01, col02, col03 = st.columns((1,1, 1))
with col02:
    Titulo_Principal = '<p style="font-weight: bolder; color:DarkBlue; font-size: 28px;">DiMas Fernandes</p>'
    st.markdown(Titulo_Principal, unsafe_allow_html=True)
    mystyle1 =   '''<style> p{text-align:center;}</style>'''
    st.markdown(mystyle1, unsafe_allow_html=True) 
    
SubTitulo_Principal = '<p style="font-weight: bolder; color:DarkBlue; font-size: 22px;">Seção de VideoCasts e PodCasts sobre Finanças</p>'
st.sidebar.markdown(SubTitulo_Principal, unsafe_allow_html=True)
mystyle2 =   '''<style> p{text-align:center;}</style>'''
st.sidebar.markdown(mystyle2, unsafe_allow_html=True)   

st.title('')
video_file = open('FIN-001.mp4', 'rb')
st.video(video_file.read())
st.title('')

with st.chat_message("assistant"):
    SOBRE = '<p style="font-family:tahoma; color:black; font-size: 18px;"> Texto em fase de produção!</p>'
    st.markdown(SOBRE, unsafe_allow_html=True)
    mystyle3 = '''
        <style>
            p {
                text-align: justify;
            }
        </style>
        '''
    st.markdown(mystyle3, unsafe_allow_html=True)    

st.markdown("""#### Professores Responsáveis: """)
 
coluna01, coluna02, coluna03 = st.columns((1,1, 1))
with coluna01:
    st.markdown(""" * Diogo Rupolo """)
with coluna02:
    st.markdown(""" * Massaki de O. Igarashi """)
with coluna03:
    st.markdown(""" * Ricardo A. Fernandes """)