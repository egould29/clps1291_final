import pickle as pkl
import pandas as pd

# colors
with open("data/colors.pkl", "rb") as f:
    object = pkl.load(f)

colors_df = pd.DataFrame(object['dsim'], columns=object['names'])
colors_df.to_csv(r'data/colors.csv')

# traits
with open("data/traitData.pkl", "rb") as f:
    object = pkl.load(f)

traits_df = pd.DataFrame(object['data'], columns=object['names'])
traits_df.to_csv(r'data/traitData.csv')