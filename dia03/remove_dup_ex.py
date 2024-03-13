# %%
import pandas as pd 

df = pd.read_excel("../data/transactions.xlsx")
df

# %%

df = df.sort_values(by='DtTransaction', ascending=False)
ultimas_transacoes = df.groupby('IdCustomer').first()
ultimas_transacoes
# Exibir as últimas transações de cada registro


# %%
condicao =  df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df[condicao]

