import streamlit as st
import openai
from streamlit_chat import message
from PIL import Image # Lib para carregar imagem no Streamlit
from gtts import gTTS #Lib para Conversão Text2Voice. Em seguida pode usar OpenAI para converter voice para texto
import os

#openai.api_key = "YOUR_API_KEY"
openai.api_key = "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"

def api_calling(prompt):
	completions = openai.Completion.create(
        engine="text-davinci-003",
		prompt=prompt,
		max_tokens=1024,
		n=1,
		stop=None,
		temperature=0.5,
	)
	message = completions.choices[0].text
	return message

def get_text():
	input_text = st.text_input("Digite sua pergunta aqui 👇", key="input")
	return input_text
    
col01, col02, col03 = st.columns((1,1, 1))
with col02:
    Titulo_Principal = '<p style="font-weight: bolder; color:DarkBlue; font-size: 28px;">DiMas Fernandes</p>'
    st.markdown(Titulo_Principal, unsafe_allow_html=True)
    mystyle1 =   '''<style> p{text-align:center;}</style>'''
    st.markdown(mystyle1, unsafe_allow_html=True) 
    
SubTitulo_Principal = '<p style="font-weight: bolder; color:DarkBlue; font-size: 22px;">VideoCasts e PodCasts com Inteligência Artificial</p>'
st.sidebar.markdown(SubTitulo_Principal, unsafe_allow_html=True)
mystyle2 =   '''<style> p{text-align:center;}</style>''' 
st.sidebar.markdown(mystyle2, unsafe_allow_html=True)   

st.title('')
video_file = open('DiMasFernandes000.mp4', 'rb')
st.video(video_file.read())
st.title('')
with st.chat_message("assistant"):
    SOBRE = '<p style="font-family:tahoma; color:black; font-size: 18px;">Olá! Eu sou o DiMas Fernandes, um avatar de Inteligência Artificial para produzir conteúdos sobre Cálculo, Linguagem de Programação e  Finanças referente às componentes curriculares dos professores Diogo, Massaki e Ricardo Fernandes. Espero que você goste do nosso conteúdo produzido.</p>'
    st.markdown(SOBRE, unsafe_allow_html=True)
    mystyle2 = '''
        <style>
            p {
                text-align: justify;
            }
        </style>
        '''
    st.markdown(mystyle2, unsafe_allow_html=True)    
st.title('')
#video_file = open('DiMasFernandes1.mp4', 'rb')
#st.video(video_file.read())
#st.title('')
#Vìdeo e Mensagem sobre a Fran
#with st.chat_message("assistant"):
#    SOBRE_A_FRAN = '<p style="font-family:tahoma; color:black; font-size: 18px;">Para ajudar na sua trajetória de estudo, eu convidei a minha amiga Fran, que também está aqui, nesta mesma plataforma, e direcionará sua pergunta ao ChatGPT 3, apresentando a resposta da plataforma, por intermédio da API OpenAI.</p>'
#    st.markdown(SOBRE_A_FRAN, unsafe_allow_html=True)
#    mystyle3 = '''
#        <style>
#            p {
#                text-align: justify;
#            }
#        </style>
#        '''
#    st.markdown(mystyle3, unsafe_allow_html=True)  


st.markdown("""#### Professores Responsáveis: """)
coluna01, coluna02, coluna03 = st.columns((1,1, 1))
with coluna01:
    st.markdown(""" * Diogo Rupolo """)
with coluna02:
    st.markdown(""" * Massaki de O. Igarashi """)
with coluna03:
    st.markdown(""" * Ricardo A. Fernandes """)

st.sidebar.success("A Plataforma DiMas Fernandes - v1.0 foi desenvolvida pelo professor Massaki de O. Igarashi e corresponde ao relatório de uma Iniciativa de Aprendizagem Transformadora - IAT com foco em desenvolver a habilidade socioemocional Comunicação, uma das 6 Habilidades Socioemocionais que compõe o Mack STLR")
link='Para mais informações acesse [Mack STLR](https://www.mackenzie.br/centro-de-excelencia-em-ensino-e-aprendizagem-transformadora/menu/sobre/mackstlr)'
st.sidebar.write(link,unsafe_allow_html=True)
st.sidebar.title('')
st.sidebar.title('')
Versao = '<p style="font-weight: bolder; color:Blue; font-size: 16px;">DiMas Fernandes - Atualização 22/out/23</p>'
st.sidebar.markdown(Versao, unsafe_allow_html=True)
mystyle3 =   '''<style> p{text-align:center;}</style>''' 
st.sidebar.markdown(mystyle3, unsafe_allow_html=True) 
