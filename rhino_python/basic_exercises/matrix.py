import rhinoscriptsyntax as rs
import random as rnd

breite = 10
laenge = 20

linien=[]
for i in range(breite):
    punkte=[]
    for j in range(laenge):
        punkte.append([i,j,rnd.random()*j/10])
    linien.append(rs.AddPolyline(punkte))
    
rs.AddLoftSrf(linien,loft_type=2)