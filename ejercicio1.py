# Ejercicio 1 (10 puntos)
# Calcule integral de exp(x) entre 0 y 1 con el método de trapecio y de Simpson.
# Haga una grafica (error.png) del error fraccional entre la solución numérica y 
# analítica como funcion del numero de puntos (desde N=10 hasta N=10^8). 
# Tanto el error como el numero de puntos deben variar en escala logaritmica.

from numpy import *
#import plotly
#from matplotlib import pyplot
#from matplotlib import savefig

def integralexp(n):
    equis=[]
    efe=[]
    # x in range (0,1) according to the assigment
    tami=float(1.0/n)
    print n
    
    for ke in range(0,n):
        equis.append(float(tami*ke))
        efe.append(float(exp(tami*ke)))
    #efe=exp(equis)
    return trapz(efe,equis)    

tam=8
plx=[]
ply=[]
vali=0

fp=open("integrales.txt","w")
for ke in range(1,tam-1):
    if ke == 1:
        vali=10
    if ke == 2:
        vali=int(10e2)
    if ke == 3:
        vali=int(10e3)
    if ke == 4:
        vali=int(10e4)
    if ke == 5:
        vali=int(10e5)
    if ke == 6:
        vali=int(10e6)
    if ke == 7:
        vali=int(10e7)
    if ke == 8:
        vali=int(10e8)

    ply.append(integralexp(vali))
    plx.append(vali)

    fp.write("%f %f\n" % (vali,ply[ke-1]))
fp.close()    
#savefig(pyplot(plx,ply))

#solucion analitica
val=exp(1)-1

#archivo para grafica de fraccion vrs. el numero de puntos
fp=open("plot.dat","w")
for ke in range(0,len(plx)):
    fp.write("%f %f\n" % (plx[ke],ply[ke]/val))
fp.close()



