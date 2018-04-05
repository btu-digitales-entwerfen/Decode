import rhinoscriptsyntax as rs
import random

breite=20
laenge=10
linien=[]
for i in range(breite):
    points=[]
    for j in range(laenge):
        faktor=abs(j-laenge/2)
        points.append([i,j,random.random()/(faktor+1)])
    linien.append(rs.AddPolyline(points))
   

rs.AddLoftSrf(linien, loft_type=2)
