# %%
import pandas as pd
import numpy as np 

data = { 
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"], 
   "idade":[31,32,34,12,np.nan], 
   "renda":[np.nan,3245,357,12432,np.nan], 
}
df = pd.DataFrame(data)
df

# %%
# contanto quantos dados faltantes existem na idade
df["idade"].isna().sum()

# %%
# contanto quantos dados faltantes existem
df.isna().sum()

# %%
df.isna().mean()

# %%
# como preencher esses vazios com o nan
df.fillna(0) #preenchendo com zero

# %%
# aqui preencher com a media das idades
df.fillna({"idade": df["idade"].mean()})

# %%
# com a media da renda e preenchido os valores vazios 
df.fillna({"renda": df["renda"].mean()})

# %%
# usando o dropna, remove as linhas com na
# all e todas as linha devem ser nan e any pelo menos uma 
df.dropna(subset=["idade", "renda"], how='all') 

# %% 
df.dropna(axis=1, thresh=2)