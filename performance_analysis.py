import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

brico_sellin = pd.read_csv("bricomarche_sell_in_22_23.csv")
brico_visites = pd.read_csv("bricomarche_visites_annuelles_22_23.csv")

data = pd.merge(brico_sellin, brico_visites, on='Code du Point de Vente')
data['Investissements_Total'] = data['BUDGET\nACCORD\nHT €'].astype(float)  

cluster_data = data[['Total\nannuel\n2023', 'Investissements_Total', 'Total visites annuelles\n2023']]
scaler = StandardScaler()
cluster_data_scaled = scaler.fit_transform(cluster_data)

inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(cluster_data_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 11), inertia, marker='o')
plt.title('Méthode Elbow')
plt.xlabel('Nombre de clusters')
plt.ylabel('Inertie')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(cluster_data_scaled)

data['Cluster'] = clusters

sns.scatterplot(x='Investissements_Total', y='Total\nannuel\n2023', hue='Cluster', data=data, palette='Set2')
plt.title('Clusters des points de vente')
plt.show()