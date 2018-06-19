# Ejercicio 1 (10 puntos)
# Calcule integral de exp(x) entre 0 y 1 con el método de trapecio y de Simpson.
# Haga una grafica (error.png) del error fraccional entre la solución numérica y 
# analítica como funcion del numero de puntos (desde N=10 hasta N=10^8). 
# Tanto el error como el numero de puntos deben variar en escala logaritmica.

def integral(

tam=8
for ke in range(1,tam+1):
  if ke == 1:
      vali=10
  if ke == 2:
      vali=10e2
  if ke == 3:
      vali=10e3
  if ke == 4:
      vali=10e4
  if ke == 5:
      vali=10e5
  if ke == 6:
      vali=10e6
  if ke == 7:
      vali=10e7
  if ke == 8:
      vali=10e8
  


