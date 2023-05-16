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

nlp = spacy.load('pt_core_news_lg')
# nlp = spacy.load(os.path.join(os.path.dirname(__file__), 'data/pt_core_news_lg-3.5.0/pt_core_news_lg/pt_core_news_lg-3.5.0'))

import json

df = None
df_desagrupado = None
df_agruapado = None

def loadDB():

    global df
    global df_desagrupado
    global df_agruapado

    # if df is None:
    #     with open('/home/wemy/Documents/luciano-pedroso/data/DataSet_.json', 'r', encoding='utf-8') as f:
    #         dados_json = json.load(f)
    #
    #     # Transforme JSON em DataFrame
    #     df = pd.DataFrame(dados_json)

    df = pd.read_parquet(os.path.join(os.path.dirname(__file__), 'data/DataSet_.gzip'))
    df_desagrupado = df

    # Construção Calculo frequencia palavras
    resposta = []
    for d in range(len(df_desagrupado['Texto'])):
        resposta.append([Counter(df_desagrupado['Texto'][d])])

    df_desagrupado['Counter'] = resposta

    # Unificando DataSet
    texto = []
    autor = []
    anos = list(df_desagrupado['Ano'].unique())
    for i in range(len(anos)):
        df_aux = df_desagrupado[df_desagrupado['Ano'] == anos[i]].reset_index(drop=True)

        # Unindo textos do mesmo ano
        text_aux = []
        for j in range(len(df_aux['Texto'])):
            a = list(df_aux['Texto'][j])
            text_aux.append(a)

        # text_aux1 = ' , '.join(text_aux)

        text_aux1 = sum(text_aux, [])
        texto.append(text_aux1)

        # Unindo Autores do mesmo ano
        autor_aux = []
        for k in range(len(df_aux['Autor'])):
            b = df_aux['Autor'][k]
            autor_aux.append(b)

        autor_aux1 = ' , '.join(autor_aux)
        autor.append(autor_aux1)

        # Construção DataSet unificado por ano

    dic_unificado = {
        'Texto': texto,
        'Ano': anos,
        'Autor': autor
    }

    df_agruapado = pd.DataFrame(dic_unificado)
    df_agruapado['Texto'] = df_agruapado['Texto'].apply(lambda x: [str(i).lower() for i in x])

    # Construção Calculo frequencia palavras
    resposta = []
    for d in range(len(df_agruapado['Texto'])):
        resposta.append([Counter(df_agruapado['Texto'][d])])

    df_agruapado['Counter'] = resposta


def processar2(lista_palavras):
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


def processar(lista_palavras):

    loadDB()
    global df
    global df_desagrupado
    global df_agruapado

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

    # Lista todos anos
    anos = list(df_agruapado['Ano'].unique())
    for i in range(len(anos)):
        anos[i] = str(anos[i])

    # Função calculo de palavras para cada ano
    def qtd_palavras_por_ano(palavra):
        qtd = []
        a = palavra
        for i in range(len(df_agruapado['Ano'])):
            b = df_agruapado['Counter'][i][0][a]
            qtd.append(b)

        return qtd

    # Frequencia de palavras
    freq_palavras = []
    for i in range(len(lista_palavras_lema)):
        a = qtd_palavras_por_ano(lista_palavras_lema[i])
        freq_palavras.append(a)

    # função referencia
    def function_ref(palavra):
        ref = []
        ano_ref = []
        for i in range(len(df_desagrupado['Texto'])):
            if df_desagrupado['Counter'][i][0][palavra] > 0:
                c = df_desagrupado['Autor'][i]
                d = str(df_desagrupado['Ano'][i])
                ano_ref.append(d)
                ref.append(c)
            else:
                c = "null"
                d = str(df_desagrupado['Ano'][i])
                ano_ref.append(d)
                ref.append(c)

        dic_ref_aux = {
            "ano": ano_ref,
            "ref": ref
        }

        df_ref = pd.DataFrame(dic_ref_aux)
        df_ref = df_ref.drop_duplicates()

        # Unindo DataSet
        autor = []
        anos = list((df_ref['ano']).unique())
        for i in range(len(anos)):
            df_aux = df_ref[df_ref['ano'] == anos[i]].drop_duplicates().reset_index(drop=True)

            # Unindo Autores do mesmo ano
            autor_aux = []
            for k in range(len(df_aux['ref'])):
                b = df_aux['ref'][k]
                autor_aux.append(b)

            autor_aux1 = ' , '.join(autor_aux)
            autor.append(autor_aux1)

        autores = []
        for i in range(len(autor)):
            if autor[i] != "null":
                a = autor[i].replace("null , ", "").replace(" , null", "")
                autores.append([a])
            else:
                a = None
                autores.append(a)

        return autores, anos

    # referencias
    lista_ref = []
    ano_ref_final = []
    for i in range(len(lista_palavras_lema)):
        a, b = function_ref(lista_palavras_lema[i])
        lista_ref.append(a)
        ano_ref_final.append(b)

    # Dicionario final
    dic_dataset = []
    for i in range(len(freq_palavras)):
        dic_aux = {
            "palavra": str(lista_palavras_lema[i]),
            "qtd": freq_palavras[i],
            "ref": lista_ref[i]
        }
        dic_dataset.append(dic_aux)

    dic_plot = {
        "anos": [int(n) for n in df_agruapado['Ano'].unique()],
        "dataset": dic_dataset,
    }

    return dic_plot
