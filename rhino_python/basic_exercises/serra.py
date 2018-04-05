import rhinoscriptsyntax as rs

#Baue Objekt anhand einer vorgezeichneten Kurve
leitkurve=rs.GetObject("leitkurve",4)#4 waehlt nur Kurven
leitkurve2=rs.CopyObject(leitkurve,[6,0,40])
serra=rs.AddLoftSrf([leitkurve,leitkurve2])

#####################
#Zentrum ermitteln
#####################

zentrum=rs.SurfaceAreaCentroid(serra)
zentrumPunkt=rs.AddPoint(zentrum[0])

#baue Fuszabdruck
zweiteKurve=rs.AddLine(rs.CurveStartPoint(leitkurve),rs.CurveEndPoint(leitkurve))
abdruck=rs.AddLoftSrf([leitkurve,zweiteKurve])

#projektion Punkt
projektion=rs.ProjectPointToSurface(zentrumPunkt,abdruck,[0,0,-1])
rs.DeleteObject(abdruck)
if projektion:
    print "Objekt steht"
    rs.ObjectColor(serra,[0,255,0])
else:
    print "Objekt steht nicht"
    rs.ObjectColor(serra,[255,0,0])