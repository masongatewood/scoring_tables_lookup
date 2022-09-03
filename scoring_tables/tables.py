from tabula import read_pdf
import pandas as pd

file = 'WA_scoring_outdoors.pdf'

def tables(pages):
    dfs = read_pdf(file, pages=pages, multiple_tables=False)
    return pd.DataFrame(dfs[0])

middle_distance = tables('39-66')
distance = tables('69-96')
combined_distance = pd.merge(middle_distance, distance, how='inner', on=['Points', 'Points'])

combined_distance['Points'] = combined_distance['Points'].astype('string')
print(combined_distance.loc[combined_distance['Points']=='1270'])

