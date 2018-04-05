import rhinoscriptsyntax as rs

linie = rs.GetObject("linie",4)

rs.AddPipe(linie,[0,0.5,1],[2,1,2],cap=2)