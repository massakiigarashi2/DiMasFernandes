import streamlit as st
from PIL import Image
import time
import openai
openai.api_key = "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"
MODEL = "gpt-3.5-turbo"
        
#image01 = Image.open('background1.PNG')

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Dimas Fernandes BOT")

form = st.form('Formulario')
pergunta = form.text_input('Digite aqui sua pergunta: ')
submit = form.form_submit_button('✔️ ENVIAR')
if submit:
    CONTENT = pergunta
    response = openai.ChatCompletion.create(model=MODEL, messages=[{"role": "user", "content": CONTENT}])
    #st.write(response.choices[0].message.content)
    with st.chat_message("user"):
        st.write(str(pergunta) + "❓")

    with st.chat_message("assistant"):
        st.write(response.choices[0].message.content)

	