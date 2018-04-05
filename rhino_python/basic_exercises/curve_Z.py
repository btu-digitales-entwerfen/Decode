import rhinoscriptsyntax as rs

linie=rs.AddCurve([[-4,0,0],[-3,3,0],[-1,1,0],[0,4,0]],degree=4)
punkt=rs.EvaluateCurve(linie,rs.CurveParameter(linie,0.7))

p=rs.AddPoint(punkt)
curvePoint=rs.AddPoint(punkt[0],punkt[1],rs.CurveLength(linie)/2)

newCurve=rs.AddInterpCurve([rs.CurveStartPoint(linie),curvePoint,rs.CurveEndPoint(linie)])