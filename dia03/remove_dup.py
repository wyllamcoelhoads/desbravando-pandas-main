# %%
import pandas as pd


# %%

data = { "Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"], 
        "Idade": [32,33,2,33,31,32],
        
}

# %%
df = pd.DataFrame(data)
df.drop_duplicates()