import matplotlib.pyplot as plt

x1 = [0,1]
y1 = [0,20]
x2 = [4,3]
y2 = [0,20]

plt.plot(x1, y1, label="Chris", linewidth=0.5, color="red")
plt.plot(x2, y2, label="lijn 2", linewidth=0.5, color="red")

n=75
stapX1=(x1[1]-x1[0])/n
stapY1=(y1[1]-y1[0])/n
stapX2=(x2[0]-x2[1])/n
stapY2=(y2[0]-y2[1])/n
#print("stapX1: " + str(stapX1))
#print("stapY1: " + str(stapY1))
#print("stapX2: " + str(stapX2))
#print("stapY2: " + str(stapY2))

while n>=0:
    xLijn=[(x1[0]+n*stapX1),(x2[1]+n*stapX2)]
    yLijn=[(y1[0]+n*stapY1),(y2[1]+n*stapY2)]
    plt.plot(xLijn, yLijn, color="green", linewidth=0.5)
    print(yLijn)
    n=n-1
plt.show()
#plt.legend()
