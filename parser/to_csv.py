import os
import pandas as pd


folder_path = 'data/images'
file_names = os.listdir(folder_path)
df = pd.DataFrame(columns=['Path', 'Label'])

for file_name in file_names:
    df.loc[-1] = [file_name, None]
    df.index = df.index + 1 

df.to_csv('data/images.csv', sep=";",index=False)