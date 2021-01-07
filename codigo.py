#Método para calcular o IMC
def CalcularIMC(AlturaPeso):
  imc = AlturaPeso[0] / (AlturaPeso[1] ** 2)
  print(f'O IMC calculado foi {imc:.2f}')

#Informe Altura e Peso
vAlturaPeso = [63.0, 1.70]

#Cálculo do IMC informado 
CalcularIMC(vAlturaPeso)