import pandas as pd
import pgeocode
import folium

brico_visites = pd.read_csv("bricomarche_visites_annuelles_22_23.csv")
leroy_visites = pd.read_csv("leroy_visites_annuelles_22_23.csv")

nomi = pgeocode.Nominatim('fr')

brico_visites.Ville = brico_visites.Ville.replace({
    "OLORON SAINTE MARIE": "Oloron-Sainte-Marie", 
    "ST JULIEN EN GENEVOIS": "Saint-Julien-en-Genevois"
})

leroy_visites.Ville = leroy_visites.Ville.replace({
    "ANNEMASSE CEDEX": "Annemasse", 
    "TASSIN LA DEMI LUNE": "Tassin-la-Demi-Lune",
    "CESSON CEDEX": "Cesson",
    "LIVRY GARGAN": "Livry-Gargan",
    "ST OUEN CEDEX": "Saint-Ouen",
    "ST DENIS": "Saint-Denis",
    "VITRY SUR SEINE": "Vitry-sur-Seine",
    "CHATEAUROUX": "Châteauroux",
    "MERIGNAC": "Mérignac",
    "CHAMBRAY LES TOURS": "Chambray-lès-Tours",
    "LA ROCHE SUR YON": "La Roche-sur-Yon",
    "ST JEAN DE VEDAS": "Saint-Jean-de-Védas",
    "NIMES": "Nîmes"
})

def get_coordinates(postal_code, city):
    location = nomi.query_postal_code(postal_code)

    if str(location.latitude) == "nan" or str(location.longitude) == "nan":
        location = nomi.query_location(city)
        if location.empty:
            return None, None
        else:
            location = location.iloc[0]

    return location.latitude, location.longitude

def format_city_name(city):
    if "CEDEX" in city:
        city = city.split(" CEDEX")[0]
    if "ST" in city:
        city = city.replace("ST", "SAINT")
    elif " " in city:
        city = city.replace(" ", "-")

    return city

brico_visites["Code Postal"] = brico_visites["Code Postal"].apply(lambda x: "0" + str(x) if len(str(x)) == 4 else x)
brico_visites["latitude"], brico_visites["longitude"] = zip(*brico_visites[["Code Postal", "Ville"]].apply(lambda x: get_coordinates(x.iloc[0], x.iloc[1]), axis=1))
brico_visites_missing_coords = brico_visites[brico_visites["latitude"].isna() | brico_visites["longitude"].isna()]

leroy_visites["Code Postal"] = leroy_visites["Code Postal"].apply(lambda x: "0" + str(x) if len(str(x)) == 4 else x)
leroy_visites["latitude"], leroy_visites["longitude"] = zip(*leroy_visites[["Code Postal", "Ville"]].apply(lambda x: get_coordinates(x.iloc[0], x.iloc[1]), axis=1))
leroy_visites_missing_coords = leroy_visites[leroy_visites["latitude"].isna() | leroy_visites["longitude"].isna()]

m = folium.Map(location=[brico_visites["latitude"].mean(), brico_visites["longitude"].mean()], zoom_start=6)

brico_logo = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAA9UlEQVR4AWJwL/ABdFu3MAzCQBiG1TJPcBMLm5zPgsZnpl7h6iV6ugKv0Lgh5s0SNLaZw9ahuk+caMhazJUExKMQb/oXblXbCOrjKYECKujAQMUSpMADaujBgP2j4ww+PREDHX0vuFf4hQZKKCDZ0aU5Xw4+UYL37KpAewwguYMvsAskZ7AFSzQMZARLRtpi9mDunq0TnSCNERSQEQFT1BWSiViH4D/DMBUrqEAQOVtpFuUMA09Gxgi2IImarTBf8ww15y19L8Q+kHFemjRkZzONZ7bh/uMncIMyMNs0nMEabICBmjNYgiW9O9u4T4F9Szc5ef8AZXxcam4d81EAAAAASUVORK5CYII="
leroy_logo = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAOVBMVEVMaXF3uyJ5uyB5uyB5uyB5uyCCvzDe78n////9/vzN5q2FwTbZ7cF+vinR6LTg78zn89iSyEuhz2XtFHBBAAAACHRSTlMAGqbm/+rR1H914LkAAAB8SURBVHgB1dO3AcMwAANBhldm3n9Yu4Sy1Nnf4loYY53nJO/sd++4qLPG0Q/jSUOPMx7dtwJvYLwIfhFM0zWYlyVcgRmI4RwkUKFAdoj5GATYCgWyixAQIirKFuSIxlIE6K5CQYVt7R0IddnUioDz/gXcHuf2erfnvbv/B1LeG0Q1rEydAAAAAElFTkSuQmCC"

for i in range(len(brico_visites)):
    marker_size = 20 - int(brico_visites["Total visites annuelles\n2023"][i])*2
    folium.Marker(
        [brico_visites["latitude"][i], brico_visites["longitude"][i]], 
        popup=brico_visites["Ville"][i],
        icon=folium.CustomIcon(brico_logo, icon_size=(marker_size, marker_size))
    ).add_to(m)

for i in range(len(leroy_visites)):
    marker_size = 30 - int(brico_visites["Total visites annuelles\n2023"][i])*2
    folium.Marker(
        [leroy_visites["latitude"][i], leroy_visites["longitude"][i]], 
        popup=leroy_visites["Ville"][i],
        icon=folium.CustomIcon(leroy_logo, icon_size=(marker_size, marker_size))
    ).add_to(m)

m.save("carte.html")