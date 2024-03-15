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
df_summary =  df.groupby(["IdCustomer"])["Points"].sum()
df_summary.reset_index()

# %%
# calculando a frequencia com o count 

(df.groupby(["IdCustomer"])
    .agg({"Points": "sum",
          "UUID": "count",
          "DtTransaction": "max"})
    .rename(columns={
        "Points": "Valor",
        "UUID": "Frequencia",
        "DtTransaction": "UltimaData"
    })
    .reset_index()
 )
# %%
from dateutil import relativedelta
import datetime


# %%
data1 = df["DtTransaction"][0]
now = datetime.datetime.now()

(now - data1).days

# %%
(datetime.datetime.now() - df["DtTransaction"][0]).days

# %%
condicao = df["IdCustomer"] == 'fe348fe6-a2f7-4f3f-b932-c10ad0b5692e'
df_user = df[condicao]
diff = datetime.datetime.now() - df_user["DtTransaction"].max()
diff.days

# %%
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days

(df.groupby(["IdCustomer"])
    .agg({"Points": "sum",
          "UUID": "count",
          "DtTransaction": recencia
          })
    .rename(columns={
        "Points": "Valor",
        "UUID": "Frequencia",
        "DtTransaction": "UltimaData"
    })
    .reset_index()
 )
