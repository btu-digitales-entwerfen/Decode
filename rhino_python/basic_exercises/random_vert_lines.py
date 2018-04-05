import rhinoscriptsyntax as rs
from random import randint as rn
import math

def baumBau(punkte):#Funktion zum BaumBau
    for punktA in punkte:
        punktB=rs.CopyObject(punktA,[0,0,rn(2,10)])
        rs.AddLine(punktA,punktB)
        rs.DeleteObject(punktB)

punkte=[rs.AddPoint(rn(0,10),rn(0,10), 0) for i in range(10)]#erzeuge zufaellige Punkte aus
baumBau(punkte)