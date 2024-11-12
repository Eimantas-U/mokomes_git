import matplotlib.pyplot as plt

 
# Tėvų surašymas (reikia pakeisti kad būtų kaip per genetikos pratybas)
P1 = ['bb++', '++ee']

# Visų genotipų surašymas (atmetant besidvigubinančius genotipus)
G1 = list(set([
    P1[0][0] + P1[0][2], P1[0][0] + P1[0][3],
    P1[0][1] + P1[0][2], P1[0][1] + P1[0][3],
    P1[1][0] + P1[1][2], P1[1][0] + P1[1][3],
    P1[1][1] + P1[1][2], P1[1][1] + P1[1][3]
 ]))

# Pirmos kartos paskaičiavimas
F1 = [G1[0][0] + G1[1][0] + G1[0][1] + G1[1][1]]

# Antros kartos genotipai (gaunami iš F1)
G2 = [F1[0][0] + F1[0][2], F1[0][0] + F1[0][3],
      F1[0][1] + F1[0][2], F1[0][1] + F1[0][3]]

# Antros kartos paskaičiavimas
F2 = [[g1 + g2 for g2 in G2] for g1 in G2]

width = 16
height = 9
fig, ax = plt.subplots(figsize=(width, height))
ax.axis('off')

base_fontsize = 18 * (width/16)
table_scale = (width/16) * 1.8

table = ax.table(cellText=F2, colLabels=G2, rowLabels=G2, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(base_fontsize)
table.scale(table_scale * 0.5, table_scale * 1.3)  # Adjust cell size

# Adding P1, G1, and F1 as text above the table 
plt.text(0.5, 1,    f'P = {P1}', ha='center', va='top', transform=ax.transAxes, fontsize=base_fontsize)
plt.text(0.5, 0.95, f'G = {G1}', ha='center', va='top', transform=ax.transAxes, fontsize=base_fontsize)
plt.text(0.5, 0.9, f'F1 = {F1}', ha='center', va='top', transform=ax.transAxes, fontsize=base_fontsize)

plt.show()

'''
reik padaryt kad tam tikrais atvejais jei yra nustatyta atsižvelgtu į tai ar genai yra toje pačioje chromosomoje ir jei yra paskaičiuoti 
rekombinacijos tikimybe, taip kad atsižvelgtu į letalias mutacijas jei tokios yra, dar reikia padaryti kad nuspalvintu tam tikrus langelius 
pagal fenotipus bei paskaičiuotu jų santykį ,reik dar padaryti kad viskas atrodytu kaip per genetikos pratybas jei taip įmanoma, dar pabandyti 
sutvarkyti aspect ratio ir kad lentelė scalintu su juo.
'''




