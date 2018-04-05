import rhinoscriptsyntax as rs

linie = rs.GetObject("linie",4)

vector=rs.VectorCreate(rs.EvaluateCurve(linie,rs.CurveParameter(linie,0.7)),rs.CurveEndPoint(linie))

rs.MoveObject(rs.AddPoint(rs.CurveStartPoint(linie)),vector)
rs.MoveObject(rs.AddPoint(rs.CurveStartPoint(linie)),-vector)
rs.MoveObject(rs.AddPoint(rs.CurveStartPoint(linie)),-vector*10)