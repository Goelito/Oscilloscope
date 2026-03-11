import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.ion() #évite de bloquer le programme quand la fenêtre matplotlib s'ouvre

frequence = int(input("Saisir la fréquence du signal (Hz) : "))
periode = 1/frequence
fenetre = 4*periode #variable qui servira a afficher uniquement 4 période dans le graphique peu importe la fréquence du signal
frequence_echantillonnage = int(input("Saisir la fréquence d'échantillonnage (Hz) : "))

t=0 #initialisation de la variable du temps pour générer ensuite la fonction sinusoïdal
prochain_echantillonnage = 0 #variable pour que la boucle sache quand prendre le prochain point en fonction de la fréquence d'échantillonnage
nb_points = int((4 / frequence) * frequence_echantillonnage) #variable pour savoir combien de point seront affiché pour 4 périodes en fonction de la fréquence d'échantillonnage

print(nb_points)

points=[]
temps=[]

fig, ax = plt.subplots() #Initialisation de la fenêtre matplotlib
line, = ax.plot([], [], 'b-o', markersize=4) #on créer une ligne invisible sur laquelle on va venir placer les points
ax.set_ylim(-1.2, 1.2) #on défini les ordonnées entre -1.2 et 1.2 car le sinus ne va jamais au dela 1 ou en dessous -1
ax.grid(True)

while True:
    valeur = math.sin(2*math.pi*frequence*t) #On genere BEAUCOUP de points pour imitier la fonction sin (avec la super formule)
    
    if t >= prochain_echantillonnage: #permet de savoir quand échantilloner un seul point
        points.append(valeur)
        temps.append(t)
        prochain_echantillonnage += (1/frequence_echantillonnage)
        if len(points) > nb_points: #permet de garder une fenêtre d'échantillonnage pour éviter de faire mal a la mémoire du pc lol
            points.pop(0)
            temps.pop(0)
            
    line.set_data(temps, points) #on affiche les points
    ax.set_xlim(t - (4/frequence), t) #on décale la fenêtre pour que ca affiche toujours 4 période
    plt.pause(0.001) #on fait une pause a matplotlib pour qu'il est le temps de générer tout ca
    
    t += 0.001