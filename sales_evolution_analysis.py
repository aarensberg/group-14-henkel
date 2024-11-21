import pandas as pd
import matplotlib.pyplot as plt

brico_sales = pd.read_csv("bricomarche_sell_in_22_23.csv")
leroy_sales = pd.read_csv("leroy_sell_in_22_23.csv")

ville_a_supp = ["ANAIS", "ALBON", "GARANCIERES SUR BEAUNE"]
brico_sales = brico_sales[~brico_sales["Ville"].isin(ville_a_supp)]



brico_ytd_evol_df = brico_sales[brico_sales["Total\nFamille"]=="TOTAL HENKEL"][["Code du Point de Vente", "Total\nYTD\nEvol"]]
brico_ytd_evol_df["Total\nYTD\nEvol"] = brico_ytd_evol_df["Total\nYTD\nEvol"].str.replace("%", "").str.replace(",", ".").astype(float)

brico_ytd_evol_df.sort_values("Total\nYTD\nEvol", ascending=False).plot(figsize=(20, 10), x="Code du Point de Vente", y="Total\nYTD\nEvol", kind="bar")
plt.title("Evolution YTD des ventes Henkel par point de vente Bricomarché")
plt.savefig("brico_ytd_evol.png")



leroy_ytd_evol_df = leroy_sales[leroy_sales["Total\nFamille"]=="TOTAL HENKEL"][["Code du Point de Vente", "Total\nYTD\nEvol"]]
leroy_ytd_evol_df["Total\nYTD\nEvol"] = leroy_ytd_evol_df["Total\nYTD\nEvol"].str.replace("%", "").str.replace(",", ".").astype(float)

leroy_ytd_evol_df.sort_values("Total\nYTD\nEvol", ascending=False).plot(figsize=(20, 10), x="Code du Point de Vente", y="Total\nYTD\nEvol", kind="bar")
plt.title("Evolution YTD des ventes Henkel par point de vente Leroy Merlin")
plt.savefig("leroy_ytd_evol.png")



brico_ytd_evol_df.columns = ["Code du PdV (brico)", "Evol YTD (brico)"]
leroy_ytd_evol_df.columns = ["Code du PdV (leroy)", "Evol YTD (leroy)"]

all_ytd_evol_df = pd.concat([brico_ytd_evol_df, leroy_ytd_evol_df], axis=1)
all_ytd_evol_df["Evol YTD (all)"] = all_ytd_evol_df["Evol YTD (leroy)"].fillna(0) + all_ytd_evol_df["Evol YTD (brico)"].fillna(0)
all_ytd_evol_df[all_ytd_evol_df["Evol YTD (all)"]>0].sort_values("Evol YTD (all)", ascending=False).plot(figsize=(20, 10), y=["Evol YTD (leroy)", "Evol YTD (brico)"], kind="bar")
plt.title("Evolution YTD des ventes Henkel par point de vente Bricomarché et Leroy Merlin (positives)")
plt.savefig("all_ytd_evol_positives.png")

all_ytd_evol_df[all_ytd_evol_df["Evol YTD (all)"]<=0].sort_values("Evol YTD (all)", ascending=False).plot(figsize=(20, 10), y=["Evol YTD (leroy)", "Evol YTD (brico)"], kind="bar")
plt.title("Evolution YTD des ventes Henkel par point de vente Bricomarché et Leroy Merlin (négatives)")
plt.savefig("all_ytd_evol_negatives.png")