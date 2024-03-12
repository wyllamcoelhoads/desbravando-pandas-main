# %%
import pandas as pd
# %%

data = {
    "nome": ["teo", "nah", "lara", "maria"],
    "sobrenome": ["calvo", "ataide", "calvo","calvo"],
    "idade": [30, 32, 31, 2]
}

# %%
data["idade"][0]

# %%
df = pd.DataFrame(data)
df 

# %%
df["sobrenome"].iloc[0]

# %%
df["idade"].iloc[0]

# %%
type(df.iloc[0])

# %%

df.index

# %%

df.columns

# %%
# verificar memoria usada em memoria ram
df.info(memory_usage='deep')

# %%
df.dtypes

# %%

df.describe()

# %%

df.head(2)

# %%
df.tail(2)