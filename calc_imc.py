calcular_imc = lambda peso, altura: round(peso / (altura ** 2), 2)

classificar_imc = lambda imc: (
    "Abaixo do peso" if imc < 18.5 else
    "Peso normal" if 18.5 <= imc < 24.9 else
    "Sobrepeso" if 24.9 <= imc < 29.9 else
    "Obesidade Grau I" if 29.9 <= imc < 34.9 else
    "Obesidade Grau II (severa)" if 34.9 <= imc < 39.9 else
    "Obesidade Grau III (mórbida)"
)

peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

print(f"O seu IMC é: {imc} - {classificacao}")
