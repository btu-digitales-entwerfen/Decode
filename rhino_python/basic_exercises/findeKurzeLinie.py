import rhinoscriptsyntax as rs

def findeKurzeLinie(linien):
    laengen=[rs.CurveLength(each) for each in linien]
    return laengen.index(min(laengen))

linien=rs.GetObjects("waehle Linien:",4)

kurzeLinie=linien[findeKurzeLinie(linien)]  #linien[4]
rs.AddPoint(rs.CurveMidPoint(kurzeLinie))