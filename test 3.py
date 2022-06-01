import matplotlib.pyplot as plt # Importeren in je editor
# Ik begin met het tekenen van twee lijnen
x1 = [0,1]       # X-coördinaat begin en eind lijn 1
y1 = [0,20]      # Y-coördinaat begin en eind lijn 
x2 = [4,3]       # X'en van lijn 2
y2 = [0,20]      # Y'en van lijn 3
# Teken de lijnen
plt.plot(x1, y1, label="Chris", linewidth=0.5, color="red")
plt.plot(x2, y2, label="lijn 2", linewidth=0.5, color="red")
# De lijnen worden hierna verdeeld in n stukjes
# Daarna worden de x'en en y'en van de tussenliggende lijnen vastgelegd in arrays
n=75
stapX1=(x1[1]-x1[0])/n
stapY1=(y1[1]-y1[0])/n
stapX2=(x2[0]-x2[1])/n
stapY2=(y2[0]-y2[1])/n
#print("stapX1: " + str(stapX1))
#print("stapY1: " + str(stapY1))
#print("stapX2: " + str(stapX2))
#print("stapY2: " + str(stapY2))
# Teken de lijnen
while n>=0:
    xLijn=[(x1[0]+n*stapX1),(x2[1]+n*stapX2)]
    yLijn=[(y1[0]+n*stapY1),(y2[1]+n*stapY2)]
    plt.plot(xLijn, yLijn, color="green", linewidth=0.5)
    print(yLijn)
    n=n-1
plt.show()   # Laat het eindresultaat zien
#plt.legend()
