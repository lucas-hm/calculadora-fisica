#Este codigo solo funciona en metros y caida libre

velo0 = 0
tiempoVer= input("hay tiempo: (s/n)")
if tiempoVer == "s":
    tiempo=float(input("ingrese el tiempo: "))
    gravedad= -9.8
    velof = velo0 + (gravedad * tiempo)
    rendondear1=round(velof,2)
    print("la velocidad final y máxima es de", rendondear1, "m/s")

elif tiempoVer == "n":
    velof1=int(input("ingrese la velocidad final: (negativo porfavor) "))
    gravedad= -9.8
    tiempo1 = velo0 + velof1 / gravedad
    rendondear=round(tiempo1,2)
    print("el tiempo es ", rendondear, "s cuando su velocidad final sea de ", velof1,"m/s")
