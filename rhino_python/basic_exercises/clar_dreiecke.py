import rhinoscriptsyntax as rs
import random 
import math

breite = 10
laenge = 20

punkte=[]
for i in range(breite):
    for j in range(laenge):
        punkte.append([i,j,random.random()])
for i in range(breite-1):
    for j in range(laenge-1):
        a1=punkte[i*laenge+j]
        a2=punkte[i*laenge+j+1]
        b1=punkte[(i+1)*laenge+j]
        b2=punkte[(i+1)*laenge+j+1]
        rs.AddPolyline([a1,a2,b2,a1])
        rs.AddPolyline([a1,b1,b2,a1])