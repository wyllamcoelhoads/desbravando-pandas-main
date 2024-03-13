# %% 
import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep = ";")
df_customers

# %%
df_customers.shape

# %%
df_customers.info(memory_usage='deep')

# %%

df_customers["Points"].astype(int)

# %%

df_customers["Points"].describe()

# %%

condicao = df_customers["Points"] > 1000

df_customers[condicao]

# %%
condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]
# %%

condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
df_customers[condicao]

# %%

df_customers [["UUID", "Name"]]

# %%
df_customers.columns
# %%
colunas = df_customers.columns.tolist()
colunas.sort()

df_customers = df_customers[colunas]
df_customers
# %%
df_customers = df_customers.rename(columns= {"Names": "Nome", "Points": "Pontos"})

df_customers

# %%
df_customers.rename(columns={"UUID":"Id"}, inplace=True)
df_customers