diasParaSegundos = int(input("Digite a quantidade de Dias: ")) * 86400
horasParaSegundos = int(input("\nDigite a quantidade de Horas: ")) * 3600
minutosParaSegundos = int(input("\nDigite a quantidade de Minutos: ")) * 60
segundos = int(input("\nDigite a quantidade de Segundos: "))

segundosTotais = diasParaSegundos + horasParaSegundos + minutosParaSegundos + segundos

print("\nO total de segundos é:", segundosTotais)