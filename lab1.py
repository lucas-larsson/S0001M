#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
