#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
#%%
# Läs in data från CSV-fil
data = pd.read_csv('data/lab1/handledsomkrets_data.csv')


#%%
# Beräkna statistiska mått
handledsomkrets_varden = data['Handledsomkrets'].values

min_värde = handledsomkrets_varden.min()
max_värde = handledsomkrets_varden.max()
variationsbredd = max_värde - min_värde
median = np.median(handledsomkrets_varden)
nedre_kvartil = np.percentile(handledsomkrets_varden, 25)
övre_kvartil = np.percentile(handledsomkrets_varden, 75)
kvartilavstånd = övre_kvartil - nedre_kvartil
medelvärde = handledsomkrets_varden.mean()
standardavvikelse = handledsomkrets_varden.std()

# Skriv ut resultat
print(f"Min: {min_värde}, Max: {max_värde}, Variationsbredd: {variationsbredd}, Median: {median}")
print(f"Nedre Kvartil: {nedre_kvartil}, Övre Kvartil: {övre_kvartil}, Kvartilavstånd: {kvartilavstånd}")
print(f"Medelvärde: {medelvärde}, Standardavvikelse: {standardavvikelse}")


#%%
# Skapa ett lådagram för att visualisera data
plt.figure(figsize=(10, 6))
sns.boxplot(x=handledsomkrets_varden)
plt.title('Lådagram över Handledsomkrets')
plt.xlabel('Handledsomkrets (cm)')
plt.grid(True)
plt.savefig('data/lab1/diagrams/handledsomkrets_lådagram.png', dpi=300)
plt.show()

#%%
# Histogram med få klasser
plt.figure(figsize=(6, 4))
plt.hist(handledsomkrets_varden, bins=5, edgecolor='black')
plt.title('Histogram med få klasser')
plt.xlabel('Handledsomkrets (cm)')
plt.ylabel('Frekvens')
plt.savefig('data/lab1/diagrams/handledsomkrets_histogram.png', dpi=300)
plt.show()

# Histogram med många klasser
plt.figure(figsize=(6, 4))
plt.hist(handledsomkrets_varden, bins=20, edgecolor='black')
plt.title('Histogram med många klasser')
plt.xlabel('Handledsomkrets (cm)')
plt.savefig('data/lab1/diagrams/handledsomkrets_histogram_många_klasser.png', dpi=300)
plt.show()

# Histogram med rimligt antal klasser (kvadratroten ur antalet mätvärden)
plt.figure(figsize=(6, 4))
n_classes = round(np.sqrt(len(handledsomkrets_varden)))
plt.hist(handledsomkrets_varden, bins=n_classes, edgecolor='black')
plt.title('Histogram med rimligt antal klasser')
plt.xlabel('Handledsomkrets (cm)')
plt.savefig('data/lab1/diagrams/handledsomkrets_histogram_rimligt_antal_klasser.png', dpi=300)
plt.show()

#%%
# Jämförande lådagram för handledsomkrets mellan män och kvinnor
plt.figure(figsize=(10, 6))
sns.boxplot(x='Kön', y='Handledsomkrets', data=data)
plt.title('Jämförande Lådagram för Handledsomkrets mellan Män och Kvinnor')
plt.xlabel('Kön')
plt.ylabel('Handledsomkrets (cm)')
plt.grid(True)
plt.savefig('data/lab1/diagrams/handledsomkrets_jamforande_ladogram.png', dpi=300)
plt.show()

#%%
# Analysera skillnaden mellan dominant och icke-dominant sida
# Skapa en pivot-tabell för att ordna datan så att varje persons dominant och icke-dominant mått står på samma rad
pivot_data = data.pivot_table(index='Person_ID', columns='Dominans', values='Handledsomkrets', aggfunc='first')
pivot_data['Differens'] = pivot_data['Dominant'] - pivot_data['Icke-dominant']

# Beräkna medelvärde och standardavvikelse för differensen
mean_diff = pivot_data['Differens'].mean()
std_diff = pivot_data['Differens'].std()

# Utför ett t-test för att se om genomsnittlig skillnad är signifikant skild från 0
t_stat, p_value = stats.ttest_1samp(pivot_data['Differens'], 0)

# Skapa ett låddiagram för att visualisera differenserna
plt.figure(figsize=(10, 6))
plt.boxplot(pivot_data['Differens'], vert=False, patch_artist=True)
plt.xlabel('Differens i Handledsomkrets mellan Dominant och Icke-dominant Sida')
plt.title('Låddiagram över Differensen i Handledsomkrets')
plt.grid(True)
plt.savefig('data/lab1/diagrams/skillnand', dpi=300)
plt.show()

# Skriv ut resultat för skillnaden mellan sidor
print(f"Medelvärde av Differens: {mean_diff}, Standardavvikelse av Differens: {std_diff}, p-värde: {p_value}")
