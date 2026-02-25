escolha = 0
num1 = int(input("informe um numero: "))
num2 = int(input("informe outro numero: "))

while escolha != 5:
    print ("""Agora escolha a opção desejada:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa""")
    escolha = int(input("Digite sua opção: "))
    if escolha == 1:
        soma = num1 + num2
        print (f"A soma dos dois números é {soma}.")
    elif escolha == 2:
        multi = num1 * num2
        print (f"A multiplicação dos dois número gerou {multi} como resultado.")
    elif escolha == 3:
        if num1 > num2:
            maior1 = num1
            print(f"o maior número é: {maior1}")
        elif num1 < num2:
            maior2 = num2
            print (f"o maior número é: {maior2}")
        else:
            print("Não há um número maior, pois estes números são iguais")
    elif escolha == 4:
        num1 = int(input("informe um novo numero: "))
        num2 = int(input("informe outro novo numero: "))
    elif escolha == 5:
        print ("ok, se precisar é só me chamar novamente. Fim do programa")
    else:
        print ("opção inválida, tente novamente")