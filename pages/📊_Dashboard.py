import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import altair as alt
#import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import datetime
import numpy as np
#https://stackoverflow.com/questions/65577892/error-message-http-not-defined-api-import-python
import urllib3
from urllib3 import request
# json data
#import json

st.set_page_config(page_title="Painel_Analítico", page_icon="📊")

st.markdown("# Índice de Satisfação")
st.sidebar.success("Índice de Satisfação")

#@st.cache_data
def get_data():
    http = urllib3.PoolManager()
    rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vToT79VG5Elh9ywpqdaBPBNXtq7yTNnM_JnCuUJvib7LTDMnlrQCMrkYSQLKE9oK_z4x504ZUd88W5X/pub?gid=1995100581&single=true&output=csv')
    dataD = rD.content
    dfD = pd.read_csv(BytesIO(dataD), index_col=0)
    dfD.columns = ['Opiniao', 'Mensagem']
    NregD = len(dfD)
    summary1 = dfD.dropna(subset=['Mensagem'], axis=0)['Mensagem']
    selecao01D = dfD['Opiniao']=='um Elogio'
    df01D = dfD[selecao01D]
    selecao02D = dfD['Opiniao']=='uma Sugestão'
    df02D = dfD[selecao02D]
    selecao03D = dfD['Opiniao']=='uma Crítica'
    df03D = dfD[selecao03D]
    return [summary1, df01D, df02D, df03D, NregD]

try:
    summary  = get_data()[0]
    Elogios  = get_data()[1]
    Sugestao = get_data()[2]
    Critica  = get_data()[3]
    TotalREG = get_data()[4]
    col1, col2, col3 = st.columns((1,1,1))
    with col1:
        pElogios = round(100*len(Elogios)/TotalREG,1)
        st.markdown("### Elogios = " + str(pElogios) + "%")
    with col2:
        pSugestao = round(100*len(Sugestao)/TotalREG,1)
        st.markdown("### Sugestão = " + str(pSugestao) + "%")
    with col3:       
        pCritica = round(100*len(Critica)/TotalREG,1)
        st.markdown("### Críticas = " + str(pCritica) + "%")
    # concatenar as palavras
    all_summary = " ".join(s for s in summary)
    # lista de stopword
    stopwords = set(STOPWORDS)
    stopwords.update(["de", "ao", "o", "nao", "para", "da", "meu", "em", "você", "ter", "um", "ou", "os", "ser", "só"])
    # gerar uma wordcloud
    wordcloud = WordCloud(stopwords=stopwords,
                          background_color="white",
                          width=1600, height=800).generate(all_summary)

    wordlist = all_summary.split()
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

    #st.info("Lista\n" + str(wordlist) + "\n")
    #st.info("Frequências\n" + str(wordfreq) + "\n")
    #st.info("Pares\n" + str(list(zip(wordlist, wordfreq))))


    form = st.form('PesquisaFatisfacao')
    
    plt.imshow(wordcloud);
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    #st.pyplot()
    wordcloud.to_file("Nuvem_de_Palavras.png")

    st.markdown("# Impressões:")
    st.pyplot() #Este método faz exibirt a nuvem de palavras
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header("Análise das Palavras:")
    chart_data = pd.DataFrame(wordfreq,wordlist)
    st.bar_chart(chart_data)

    st.info("Desenvolvido por: Equipe FabLab / Prof. Massaki Igarashi")

except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
