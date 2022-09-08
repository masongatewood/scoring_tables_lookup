from tabula import read_pdf
import pandas as pd

file = 'scoring_tables/WA_scoring_outdoors.pdf'

def tables(pages):
    dfs = read_pdf(file, pages=pages, multiple_tables=True)
    combined = pd.concat(dfs)
    return pd.DataFrame(combined)

middle_distance = tables('39-66')
distance = tables('69-96')

print(middle_distance.loc[
    (middle_distance['Mile'].str.contains('3:58'))
])