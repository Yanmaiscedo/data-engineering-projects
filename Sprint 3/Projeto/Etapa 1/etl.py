import pandas as pd
import re

df = pd.read_csv("concert_tours_by_women.csv")

df.columns = [col.strip() for col in df.columns]

df[['Start year', 'End year']] = df['Year(s)'].str.extract(r'(\d{4})(?:–|-)?(\d{4})?')
df['End year'] = df['End year'].fillna(df['Start year'])

df['Start year'] = df['Start year'].astype(int)
df['End year'] = df['End year'].astype(int)

df = df.dropna(subset=[
    'Actual gross', 
    'Adjustedgross (in 2022 dollars)', 
    'Artist', 
    'Tour title', 
    'Shows', 
    'Average gross', 
    'Start year', 
    'End year'
])

def to_float(val):
    if isinstance(val, str):
        cleaned = re.sub(r"[^\d.]", "", val)
        return float(cleaned) if cleaned else 0.0
    return val

df['Actual gross'] = df['Actual gross'].apply(to_float)
df['Adjustedgross (in 2022 dollars)'] = df['Adjustedgross (in 2022 dollars)'].apply(to_float)
df['Average gross'] = df['Average gross'].apply(to_float)

df['Shows'] = df['Shows'].astype(int)

df = df.rename(columns={"Adjustedgross (in 2022 dollars)": "Adjusted gross (in 2022 dollars)"})

df = df.sort_values(by="Adjusted gross (in 2022 dollars)", ascending=False).reset_index(drop=True)
df["Rank"] = df.index + 1

colunas_desejadas = [
    "Rank",
    "Actual gross",
    "Adjusted gross (in 2022 dollars)",
    "Artist",
    "Tour title",
    "Shows",
    "Average gross",
    "Start year",
    "End year"
]

tabela_filtrada = df[colunas_desejadas]

tabela_filtrada.to_csv("/data/csv_limpo.csv", index=False)

print("Arquivo 'csv_limpo.csv' gerado com sucesso.")
