########################################### app v1.1 #################################################
# display the query results clearly 
# pb : absence retour à la ligne pour les points virgules (ex : cheese)

import streamlit as st
import pandas as pd
from functools import reduce
import operator
import ast
import re

 
st.title("""
Welcome to frigo vide app
""")
 
df = pd.read_csv("c:\\Users\\guibe\\OneDrive\\Documents\\ENSAE\\3A\\S1\\Infra\\projet\\Projet-Infra-3A\\Data\\echant_10k_recipes.csv")

def clean(col) : 
    col2 = []
    col3 = []
    for i in col : 
        i = ast.literal_eval(i)
        col2.append(i)
    for j in col2 : 
        if len(j) == 1 : 
            col3.append(j[0].split('.'))
        else : 
            col3.append(j)
    return col3

df['clean_dir'] = clean(df['directions'])



# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search recipies by ingredients", value="")

# Filter the dataframe using masks
sentence = text_search.split(' ')
nb = len(sentence)
base = r'^{}'
expr = '(?=.*{})'
rep = df[df['NER'].str.contains(base.format(''.join(expr.format(w) for w in sentence)))][['title','NER']]
#m2 = df["Title"].str.contains(text_search)
#df_search = df[m1 | m2]

if text_search:
    st.header("Il y a", len(rep), "recettes correspondantes")
    rep['%'] = rep['NER'].apply(lambda ing: round((nb / len(ast.literal_eval(ing)))*100,1))
    for i in rep.sort_values('%', ascending=False).head(15)['title'] :
        st.write(i, "pourcentage d'ingrédients déjà à disposition", rep.sort_values('%', ascending=False)['%'])


