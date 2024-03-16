# %%

import pandas as pd

data_01 = { 
           "id": [1,2,3,4], 
           "nome":["Teo", "Mat", "Nah", "Mah"], 
           "idade": [31,31,32,32] 
}

df_01 = pd.DataFrame(data_01)
df_01


# %%

data_02 = { 
           "id": [1,2,3,4], 
           "nome":["Teo", "Mat", "Nah", "Mah"], 
           "idade": [31,31,32,32] 
}
df_02 = pd.DataFrame(data_02)
df_02

# %%
# com o concat é possivel emplinhar os df e com o res_ind e possivel corrigir o indices
# para excluir o indice antigo usamos tre em drop
pd.concat([df_01,df_02]).reset_index(drop=True)
# %%

data_03 =  {
    "sobrenome": ["Calvo", "Silva", "Costa", "Souza"],
    "renda": [3100,3100,3200,3200]
}
df_03 = pd.DataFrame(data_03)
df_03


# %%
pd.concat([df_01, df_03], axis=1)


# %%