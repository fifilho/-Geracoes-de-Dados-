import matplotlib.pyplot as graf
def rodar():
    emocoes = ["Tesao","Tedio","Felicidade","Preguiça","Sono"]
    porcentagens = [80,20,20,20,20]
    kabumm = [0.1,0,0.,0,0]

    graf.title("Minhas Emocoes")
    graf.pie(porcentagens, labels=emocoes,explode=kabumm,autopct="%.1f%%",pctdistance=0.7,startangle=90) #frame radius counterclock
    graf.show()