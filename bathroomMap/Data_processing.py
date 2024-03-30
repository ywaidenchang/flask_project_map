import pandas as pd

filepath = "Datas/bathroomData_Seoul.csv"
df = pd.read_csv(filepath, encoding="cp949").dropna()
name1 = df["대명칭"].to_list()
x1 = df["WSG84X좌표"].to_list()
y1 = df["WSG84Y좌표"].to_list()

filepath = "Datas/bathroomData_Gyeongido.csv"
df2 = pd.read_csv(filepath, encoding="cp949").dropna()
name2 = df2["화장실명"].to_list()
x2 = df2["경도"].to_list()
y2 = df2["위도"].to_list()

filepath = "Datas/bathroomData_Austrailia.csv"
df3 = pd.read_csv(filepath, encoding="latin-1").dropna()
name3 = df3["Name"].to_list()
x3 = df3["Longitude"].to_list()
y3 = df3["Latitude"].to_list()

filepath = "Datas/bathroomData_Dublin.csv"
df4 = pd.read_csv(filepath, encoding="cp949").dropna()
name4 = df4["Location"].to_list()
x4 = df4["Long"].to_list()
y4 = df4["Lat"].to_list()

filepath = "Datas/bathroomData_Caerphilly.csv"
df5 = pd.read_csv(filepath, encoding="cp949").dropna()
name5 = df5["Location (ENG)"].to_list()
x5 = df5["Long"].to_list()
y5 = df5["Lat"].to_list()

filepath = "Datas/bathroomData_London.csv"
df6 = pd.read_csv(filepath, encoding="utf-8").dropna()
name6 = df6["Name"].to_list()
x6 = df6["Longitude"].to_list()
y6 = df6["Latitude"].to_list()

filepath = "Datas/bathroomData_Edmonton.csv"
df7 = pd.read_csv(filepath, encoding="utf-8").dropna()
name7 = df7["Location Name"].to_list()
x7 = df7["Longitude"].to_list()
y7 = df7["Latitude"].to_list()

filepath = "Datas/bathroomData_Jersey.csv"
df8 = pd.read_csv(filepath, encoding="latin-1").dropna()
name8 = df8["Public toilet location"].to_list()
x8 = df8["Longitude"].to_list()
y8 = df8["Latitude"].to_list()

filepath = "Datas/bathroomData_Vadodara.csv"
df9 = pd.read_csv(filepath, encoding="utf-8").dropna()
name9 = df9["Assessor Address"].to_list()
x9 = df9["Longitude"].to_list()
y9 = df9["Latitude"].to_list()

name = name1 + name2 + name3 + name4 + name5 + name6 + name7 + name8 + name9
x = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
y = y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9
