# %%
import pandas as pd 

data_users = { 
              "id": [1,2,3,4], 
              "nome":["Teo", "Mat", "Nah", "Mah"], 
              "idade": [31,31,32,32] 
}

df_user = pd.DataFrame(data_users)
data_users

# %%

data_transacoes = { 
                   "id_user": [1,1,1,2,3,3], 
                   "vl":[432,532,123,6,4,87], 
                   "qtProdutos": [2,1,3,6,10,2] 
}

data_transacoes = pd.DataFrame(data_transacoes)
data_transacoes

# %%
# usado para verificar na tabela da esquerda os dados referente na direta
data_transacoes.merge(df_user, 
                      how="left", 
                      left_on="id_user",
                      right_on="id"
                      )

# igual a no sql abaixo
# SELECT * 
# FROM df_transaction
# LEFT JOIN id_user
# ON df_transaction.id_user = df_user.id



