# mini sistema bancario

print("Bem-vindo ao mini sistema bancário!")

# ===== LOGIN =====
# ===== LOGIN =====
usuario_correto = "pablo"
senha_correta = "1234"

while True:
    print("\n===== LOGIN =====")
    usuario = input("Digite seu usuário: ").strip().lower()
    senha = input("Digite sua senha: ").strip()

    if usuario == usuario_correto and senha == senha_correta:
        print("\nLogin realizado com sucesso!")
        break
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
# ===== BANCO =====
print("\n===== BANCO =====")
saldo = 0

while True:
    print(f"\nSaldo atual: R$ {saldo:.2f}")

    opcao = input("Digite a opção desejada:\n"
    "[1] Depositar\n"
    "[2] Sacar\n"
    "[3] Consultar Saldo\n"
    "[4] Sair\n"
    "Opção: ")

    if opcao == "1":
        while True:
            valor_deposito = float(input("Digite o valor a ser depositado: R$ "))

            if valor_deposito > 0:
                saldo += valor_deposito
                print(f"Depósito realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
                break
            else:
                print("Valor inválido. Digite um valor maior que zero.")

    elif opcao == "2":
        valor_saque = float(input("Digite o valor a ser sacado: R$ "))

        if valor_saque > 0 and valor_saque <= saldo:
            saldo -= valor_saque
            print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
        elif valor_saque <= 0:
            print("O valor do saque deve ser maior que zero.")
        else:
            print("Saldo insuficiente para realizar o saque.")

    elif opcao == "3":
        print(f"Seu saldo é: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Obrigado por utilizar nosso sistema bancário!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")
