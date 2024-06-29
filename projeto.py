# Lista para armazenar os usuários
usuarios = []

# Lista para armazenar as contas
contas = []

# Variável para controlar o número sequencial da conta
numero_conta_sequencial = 0

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
    endereco = input("Digite o endereço do usuário: ")
    
    # Verifica se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("CPF já cadastrado. Não é possível criar usuário.")
            return
    
    # Adiciona o usuário apenas se o CPF não estiver cadastrado
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")

def criar_conta():
    global numero_conta_sequencial
    
    cpf = input("Digite o CPF do usuário para criar a conta: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            numero_conta_sequencial += 1
            numero_conta = f"{numero_conta_sequencial:04}"  # Número da conta formatado para quatro dígitos com zero à esquerda
            agencia = "0001"  # Exemplo de agência fixa (pode ser ajustado conforme necessidade)
            contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo": 0, "extrato": []})
            print(f"Conta {agencia}/{numero_conta} criada com sucesso para {usuario['nome']}!")
            return
    
    print("Usuário não encontrado!")

def depositar(saldo):
    dep = input("Digite o valor que você quer depositar: ")
    if dep.isdigit():
        valor_dep = int(dep)
        saldo += valor_dep
        contas[-1]["saldo"] += valor_dep
        contas[-1]["extrato"].append(f"Depósito: R$ {valor_dep:.2f}")
        print(f"Você depositou: R$ {valor_dep:.2f}")
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
    else:
        print("Valor inválido! Digite um número.")
    return saldo

def sacar(saldo):
    saque = input("Digite o valor que você quer sacar: ")
    if saque.isdigit():
        saque = int(saque)
        if saque <= saldo:
            saldo -= saque
            contas[-1]["saldo"] -= saque
            contas[-1]["extrato"].append(f"Saque: R$ {-saque:.2f}")
            print(f"Você sacou: R$ {saque:.2f}")
            print(f"Seu saldo atual é: R$ {saldo:.2f}")
        else:
            print("Saldo insuficiente para saque.")
    else:
        print("Valor inválido! Digite um número.")
    return saldo

def ver_extrato(saldo):
    extrato = contas[-1]["extrato"]
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
        print(f"Saldo atual: R$ {saldo:.2f}")

# Exemplo de utilização:
while True:
    menu = """
    [c] Criar Conta
    [u] Criar Usuário
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
    => """
    
    opcao = input(menu)
    
    if opcao == "c":
        criar_conta()
    elif opcao == "u":
        criar_usuario()
    elif opcao == "d":
        saldo = depositar(contas[-1]["saldo"] if contas else 0)
    elif opcao == "s":
        saldo = sacar(contas[-1]["saldo"] if contas else 0)
    elif opcao == "e":
        saldo = contas[-1]["saldo"] if contas else 0
        ver_extrato(saldo)
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Escolha uma opção do menu.")

