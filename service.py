#!python -m spacy download pt_core_news_lg
import os

import pandas as pd
from collections import Counter

import nltk

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

stops = stopwords.words('portuguese')
nltk.download('wordnet')

import spacy

# nlp = spacy.load('pt_core_news_lg')
nlp = spacy.load(os.path.join(os.path.dirname(__file__), 'data/pt_core_news_lg-3.5.0/pt_core_news_lg/pt_core_news_lg-3.5.0'))

import json

df = None

def loadDB():

    global df

    # if df is None:
    #     with open('/home/wemy/Documents/luciano-pedroso/data/DataSet_.json', 'r', encoding='utf-8') as f:
    #         dados_json = json.load(f)
    #
    #     # Transforme JSON em DataFrame
    #     df = pd.DataFrame(dados_json)

    df = pd.read_parquet(os.path.join(os.path.dirname(__file__), 'data/DataSet_.gzip'))


def processar(lista_palavras):
    loadDB()
    global df

    # Transformar palavras da lista em miniscula
    lista_palavras = [x.lower() for x in lista_palavras]

    # Lematizar palavras --- parte 1
    lista_aux = []
    for elemento in lista_palavras:
        if ' ' in elemento or elemento.isspace():
            lista_aux.append('palavra_composta')
        else:
            lista_aux.append('palavra_unica')

    # Aplicando lematização nas palavras --- parte 2
    lista_palavras_lema = []
    for i in range(len(lista_palavras)):
        if lista_aux[i] == "palavra_composta":
            a = str(lista_palavras[i])
            lista_palavras_lema.append(a)
        else:
            doc = nlp(lista_palavras[i])
            a = doc[0].lemma_
            b = a.lower()
            lista_palavras_lema.append(b)

    # Montagem Json final
    # Labels
    anos = list(df['Ano'].unique())
    for i in range(len(anos)):
        anos[i] = str(anos[i])

    # Construção Calculo frequencia palavras
    resposta = []
    for d in range(len(df['Texto'])):
        resposta.append([Counter(df['Texto'][d])])

    # Função calculo de palavras para cada ano
    def qtd_palavras(palavra):
        qtd = []
        a = palavra
        for i in range(len(resposta)):
            b = resposta[i][0][a]
            qtd.append(b)

        return qtd

    # Frequencia de palavras
    freq_palavras = []
    for i in range(len(lista_palavras_lema)):
        a = qtd_palavras(lista_palavras_lema[i])
        freq_palavras.append(a)

    # Dicionario final
    dic_dataset = []
    for i in range(len(freq_palavras)):
        dic_aux = {
            "label": str(lista_palavras_lema[i]),
            "data": freq_palavras[i]
        }
        dic_dataset.append(dic_aux)

    # referencias
    refer = set()
    for i in range(len(df['Autor'])):
        a = df['Autor'][i]
        refer.add(a.replace('_', ' '))



    dic_plot = {
        "labels": anos,
        "dataset": dic_dataset,
        "referencias": list(refer)

    }

    return dic_plot
