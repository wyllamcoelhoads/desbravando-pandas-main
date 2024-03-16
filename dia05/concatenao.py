# %%

import pandas as pd

df_01 = pd.read_csv("../data/ipea/homicidios.csv", sep=";")

df_01 = df_01.rename(columns={"valor":'homicidios'})
df_01
# %%

df_02 = pd.read_csv("../data/ipea/homicidios-por-armas-de-fogo.csv", sep=";")

df_02 = df_02.rename(columns={"valor":'homicidios-por-arma-de-fogo'})
df_02



# %%
df_01 = df_01.set_index(["cod","nome","periodo"])
df_02 = df_02.set_index(["cod","nome","periodo"])


# %%
pd.concat([df_01, df_02], axis=1).reset_index()
# %%
