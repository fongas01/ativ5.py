def calculadora():
    while True:
        # Mostra o menu de operações
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        # Solicita ao usuário escolher uma opção
        escolha = input("Escolha uma operação (0-4): ")

        # Verifica a escolha do usuário
        if escolha == '0':
            print("Saindo da calculadora. Até logo!")
            break
        elif escolha in ['1', '2', '3', '4']:
            # Solicita os números para a operação
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Executa a operação escolhida
            if escolha == '1':
                resultado = num1 + num2
                print("Resultado: ", resultado)
            elif escolha == '2':
                resultado = num1 - num2
                print("Resultado: ", resultado)
            elif escolha == '3':
                resultado = num1 * num2
                print("Resultado: ", resultado)
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print("Resultado: ", resultado)
                else:
                    print("Erro: Divisão por zero!")
        else:
            print("Essa opção não existe. Tente novamente.")


# Chama a função da calculadora
calculadora()
