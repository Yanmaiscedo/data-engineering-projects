import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("csv_limpo.csv")

df["valor_por_show"] = df["Adjusted gross (in 2022 dollars)"] / df["Shows"]

most_common_artist = df["Artist"].value_counts().idxmax()
media = df[df["Artist"] == most_common_artist]["Actual gross"].mean()

one_year = df[df["Start year"] == df["End year"]]
melhor = one_year.loc[one_year["Average gross"].idxmax()]

top3 = df.nlargest(3, "valor_por_show")[["Tour title", "Artist", "valor_por_show"]]

with open("/app/volume/respostas.txt", "w") as f:
    f.write(f"Q1:\n--- {most_common_artist} com média de ${media:,.2f}\n\n")
    f.write(f"Q2:\n--- {melhor['Tour title']} ({melhor['Artist']}) com média de ${melhor['Average gross']:,.2f}\n\n")
    f.write("Q3:\n---\n")
    for _, row in top3.iterrows():
        f.write(f"{row['Tour title']} ({row['Artist']}) - ${row['valor_por_show']:,.2f}\n")


df_artista = df[df["Artist"] == most_common_artist]

faturamento_ano = df_artista.groupby("Start year")["Actual gross"].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=faturamento_ano, x="Start year", y="Actual gross", marker="o")
plt.title(f"Faturamento por ano - {most_common_artist}")
plt.xlabel("Ano de início da turnê")
plt.ylabel("Faturamento bruto (USD)")
plt.grid(True)
plt.tight_layout()
plt.savefig("/app/volume/Q4.png")
plt.close()

top5_artistas = df.groupby("Artist")["Shows"].sum().nlargest(5).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=top5_artistas, x="Artist", y="Shows", hue="Artist", palette="viridis", legend=False)
plt.title("Top 5 artistas com mais shows na lista")
plt.xlabel("Artista")
plt.ylabel("Total de Shows")
plt.tight_layout()
plt.grid(axis="y")
plt.savefig("/app/volume/Q5.png")
plt.close()
