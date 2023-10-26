import streamlit as st
import openai
from streamlit_chat import message
from PIL import Image # Lib para carregar imagem no Streamlit
from gtts import gTTS #Lib para Conversão Text2Voice. Em seguida pode usar OpenAI para converter voice para texto
import os
  
image01 = Image.open('CVprofs.JPG')
image02 = Image.open('CValunos.JPG')
image03 = Image.open('CCT20anos.PNG')
st.title("A Equipe Dimas Fernandes")  
#coluna1, coluna2 = st.columns((1,1))
#with coluna1:
st.image(image01, width=400, caption='Equipe Dimas Fernandes - Professores') 
#with coluna2:
st.image(image02, width=400, caption='Equipe Dimas Fernandes - Alunos') 
    
st.markdown("""#### Professores Responsáveis: """)
 
coluna01, coluna02, coluna03 = st.columns((1,1, 1))
with coluna01:
    st.markdown(""" * Diogo Rupolo """)
with coluna02:
    st.markdown(""" * Massaki de O. Igarashi """)
with coluna03:
    st.markdown(""" * Ricardo A. Fernandes """)

st.image(image03, width=670, caption='Equipe Dimas Fernandes - Alunos')
