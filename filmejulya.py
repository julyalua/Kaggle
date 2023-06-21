#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import mysql.connector


# In[2]:


ratings = pd.read_csv("title.ratings.tsv.gz", sep="\t")
ratings


# In[3]:


basics = pd.read_csv("title.basics.tsv.gz", sep="\t")
basics


# In[4]:


movies=basics.merge(ratings)


# In[5]:


movies


# In[10]:


movies.corr()


# In[15]:


import re
def get_first(text):
    test = re.match(r'\W*(\w[^,. !?"]*)', text).groups()[0]
    return test

movies['new'] = movies.genres.str.split(',', expand=True)[0]
movies


# In[22]:


# Import label encoder
from sklearn import preprocessing

# label_encoder object knows
# how to understand word labels.
label_encoder = preprocessing.LabelEncoder()

# Encode labels in column 'species'.
movies['new']= label_encoder.fit_transform(movies['new'])

movies['new'].unique()


# In[29]:


movies.corr()


# O intuito do trabalho é analisar a base de dados do IMDB, um site que possui uma base de dados online de informação sobre cinema, TV, música e etc. Os dataframes escolhidos para análise são os títulos de filme e as avaliações, que foram mesclados em um só dataframe para viabilizar uma análise preditiva entre as variáveis.
# Inicialmente, foi testada a relação o número de votos e o avaliação do filme de 0 a 10, no entanto, o resultado não foi satisfatório a ponto de iniciar uma regresão linear poris mostrou uma baixa correlação.
# Logo após, separamos as strings dentro da coluna de gêneros, a fim de manter somente o primeiro gênero, e assim relacionar cada gênero a um número para testar a relação númerica entre a avalição dos filmes e o seu gênero. 
# Todavia, mesmo com todas as tentativas de manipular a base de dados e encontrar uma correlação para aplicar um modelo preditivo para avaliação de filmes, não foi possível encontrar uma correlação forte o suficiente entre as variáveis disponíveis, o que inviabiliza o trabalho. 
