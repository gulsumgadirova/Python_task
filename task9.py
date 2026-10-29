eded = int(input("Ucreqemli ededi daxil et:"))
yuzluk = eded // 100
onluq = (eded // 10) % 10
teklik = eded % 10
cem = yuzluk + onluq + teklik
print ("Yuzluk:",yuzluk)
print("Onluq:",onluq)
print ("Teklik:",teklik)
print ("Reqemlerin cemi:",cem)
