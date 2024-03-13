#3.  Carregue os dados do arquivo data/ipea/homicidios.csv de forma correta e informe:
#    Quantidade de linhas
#    Quantidade de colunas
#    Nome da primeira coluna
#    Nome da última coluna
 # %%
 # Carregue os dados do arquivo data/ipea/homicidios.csv de forma correta e informe:

import pandas as pd 

df_homicidios = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
df_homicidios

# %%

# Obter a quantidade de linhas
quantidade_linhas = len(df_homicidios)
quantidade_linhas



# %%

# Obter a quantidade de colunas
quantidade_colunas = df_homicidios.shape[1]
quantidade_colunas

# %% 
primeira_coluna = df_homicidios.columns[0]
primeira_coluna 


# %%

ultima_coluna = df_homicidios.columns[-1]
ultima_coluna 

