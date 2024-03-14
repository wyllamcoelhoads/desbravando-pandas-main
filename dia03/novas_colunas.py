# %%

import pandas as pd 
import numpy as np

# %%
df = pd.read_csv("../data/customers.csv", sep=";")

# %%

df["Points_double"] = df["Points"] * 2
df
# %%
df["Points_radio"] = df["Points_double"] / df["Points"]
df

# %%

df["Constante"] = None
df
# %%

df["Points_log"] = np.log(df["Points"])
df

# %%
df['Name'].str.upper()

# %%
def get_fist(nome:str):
    return nome.split("_")[0]

# %%
df["Name_First"] = df["Name"].apply( get_fist ) 
df




# %%
