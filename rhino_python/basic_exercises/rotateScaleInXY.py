import rhinoscriptsyntax as rs

object=rs.GetObject("Select a Surface",8)

def rotateScale(surface,max):
    if max<4:
        linesSurfaceOriginal=rs.DuplicateEdgeCurves(surface)
        pointOrigin=rs.AddPoint(rs.CurveMidPoint(linesSurfaceOriginal[0]))
        #skaliere Objekt
        scaleSurface=rs.ScaleObject(surface,pointOrigin,[0.5,0.5,0.5],copy=True)
        #finde Achse
        lineScaled=rs.DuplicateEdgeCurves(scaleSurface)[2]
        rotateAxes=rs.VectorCreate(rs.CurveStartPoint(lineScaled),rs.CurveEndPoint(lineScaled))
        #drehe Objekt um den rotateAxes
        rotatedObject=rs.RotateObject(scaleSurface,rs.CurveMidPoint(lineScaled),40.0,rotateAxes)
        #Loesche unnoetige Objekte
        rs.DeleteObjects([lineScaled,pointOrigin])
        max+=1
        #hier ruft sich die Funktion selber auf bis der max == 4 ist
        rotateScale(rotatedObject,max)

rotateScale(object,0)

