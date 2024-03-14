# %%
import pandas as pd

x = [1,2,45,65,56,7,23,3,5]

series = pd.Series(x)
series.max()

# %%
# importando dados 
df = pd.read_excel("../data/transactions.xlsx")
df
# %%
condicacao = df["IdCustomer"] == "5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"

df_user = df[condicacao]
df_user['Points'].sum()

# %%
# para todos os usuarios

pontos = {}
for i in df["IdCustomer"].unique():
    condicacao = df["IdCustomer"]==i
    pontos[i] = df[condicacao]["Points"].sum()
    
pontos

# %% 
# usando o group by pra fazer a mesma coisa de cima
df.groupby(["IdCustomer"])["Points"].mean()