import pandas as pd
import matplotlib.pyplot as plt

brico_pp = pd.read_csv("bricomarche_pp22_23.csv")
brico_sales = pd.read_csv("bricomarche_sell_in_22_23.csv")

ville_a_supp = ["ANAIS", "ALBON", "GARANCIERES SUR BEAUNE"]
brico_sales = brico_sales[~brico_sales["Ville"].isin(ville_a_supp)]

leroy_pp = pd.read_csv("leroy_pp22_23.csv")
leroy_sales = pd.read_csv("leroy_sell_in_22_23.csv")

months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

plt.figure(figsize=(15, 6))
plt.plot(
    brico_sales[brico_sales["Total\nFamille"] == "TOTAL HENKEL"][[f"{month}\n{year}" for year in [2022, 2023] for month in months]].sum(), 
    color="red", marker="o")
plt.plot( 
    leroy_sales[leroy_sales["Total\nFamille"] == "TOTAL HENKEL"][[f"{month}\n{year}" for year in [2022, 2023] for month in months]].sum(), 
    color="green", marker="o")
plt.title("Ventes Bricomarché")
plt.xticks(rotation=45)
plt.legend(["Bricomarché", "Leroy Merlin"])
plt.savefig("sales_evolution_22_23.png")



brico_pp["BUDGET\nACCORD\nHT €"] = brico_pp["BUDGET\nACCORD\nHT €"].str.replace(" €", "").str.replace(",", ".").str.replace("\u202f", "").astype(float)
brico_pp_by_shop = brico_pp.groupby("CODE DU POINT DE VENTE")["BUDGET\nACCORD\nHT €"].sum()

brico_sales["Total 2022-2023"] = brico_sales["Total\nannuel\n2022"] + brico_sales["Total\nannuel\n2023"]
brico_sales_by_shop = brico_sales.groupby("Code du Point de Vente")["Total 2022-2023"].sum()

brico_pp_sales_by_shop = pd.concat([brico_pp_by_shop, brico_sales_by_shop], axis=1, join="inner")
brico_pp_sales_by_shop["ROI"] = brico_pp_sales_by_shop["Total 2022-2023"] / brico_pp_sales_by_shop["BUDGET\nACCORD\nHT €"]
brico_pp_sales_by_shop["ROI (%)"] = brico_pp_sales_by_shop["ROI"] / brico_pp_sales_by_shop["ROI"].sum() * 100

brico_pp_sales_by_shop.sort_values("ROI (%)", ascending=False).plot(kind="bar", y="ROI (%)")
plt.title("ROI par point de vente Bricomarché")
plt.savefig("brico_roi_par_magasin.png")

brico_pp_sales_by_shop.sort_values("ROI (%)", ascending=False).head(6).plot(kind="bar", y="ROI (%)")
plt.title("Meilleurs points de vente Bricomarché")
plt.savefig("brico_roi_par_magasin_top6.png")



leroy_pp["BUDGET\nACCORD\nHT €"] = leroy_pp["BUDGET\nACCORD\nHT €"].str.replace(" €", "").str.replace(",", ".").str.replace("\u202f", "").astype(float)
leroy_pp_by_shop = leroy_pp.groupby("CODE DU POINT DE VENTE")["BUDGET\nACCORD\nHT €"].sum()

leroy_sales["Total 2022-2023"] = leroy_sales["Total\nannuel\n2022"] + leroy_sales["Total\nannuel\n2023"]
leroy_sales_by_shop = leroy_sales.groupby("Code du Point de Vente")["Total 2022-2023"].sum()

leroy_pp_sales_by_shop = pd.concat([leroy_pp_by_shop, leroy_sales_by_shop], axis=1, join="inner")
leroy_pp_sales_by_shop["ROI"] = leroy_pp_sales_by_shop["Total 2022-2023"] / leroy_pp_sales_by_shop["BUDGET\nACCORD\nHT €"]
leroy_pp_sales_by_shop["ROI (%)"] = leroy_pp_sales_by_shop["ROI"] / leroy_pp_sales_by_shop["ROI"].sum() * 100

leroy_pp_sales_by_shop.sort_values("ROI (%)", ascending=False).plot(kind="bar", y="ROI (%)")
plt.title("ROI par point de vente Leroy Merlin")
plt.savefig("leroy_roi_par_magasin.png")

leroy_pp_sales_by_shop.sort_values("ROI (%)", ascending=False).head(7).plot(kind="bar", y="ROI (%)")
plt.title("Meilleurs points de vente Leroy Merlin")
plt.savefig("leroy_roi_par_magasin_top7.png")



brico_pp_sales_by_shop.columns = ["Budget Brico", "Ventes Brico", "ROI Brico", "ROI (%) Brico"]
leroy_pp_sales_by_shop.columns = ["Budget Leroy", "Ventes Leroy", "ROI Leroy", "ROI (%) Leroy"]

all_pp_sales_by_shop = pd.concat([brico_pp_sales_by_shop, leroy_pp_sales_by_shop], axis=1)
all_pp_sales_by_shop["ROI"] = all_pp_sales_by_shop["ROI Brico"].fillna(0) + all_pp_sales_by_shop["ROI Leroy"].fillna(0)
all_pp_sales_by_shop["ROI (%)"] = all_pp_sales_by_shop["ROI"] / all_pp_sales_by_shop["ROI"].sum() * 100

all_pp_sales_by_shop.sort_values("ROI (%)", ascending=False).plot(figsize=(15, 6), kind="bar", y=["ROI (%) Brico", "ROI (%) Leroy"], color=["red", "green"])
plt.title("ROI par point de vente Bricomarché et Leroy Merlin")
plt.savefig("all_roi_par_magasin.png")

all_pp_sales_by_shop.sort_values("ROI (%)", ascending=False).head(17).plot(figsize=(15, 6), kind="bar", y=["ROI (%) Brico", "ROI (%) Leroy"], color=["red", "green"])
plt.title("Meilleurs points de vente Bricomarché et Leroy Merlin")
plt.savefig("all_roi_par_magasin_top17.png")