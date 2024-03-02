import random
import string
import my_database

def gerar_senha(comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais):
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation
    
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def fazer_login():
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    if usuario in my_database.database and my_database.database[usuario] == senha:
        print("Login bem-sucedido! Bem-vindo,", usuario)
    else:
        print("Credenciais inválidas. Por favor, tente novamente.")

def registrar():
    novo_usuario = input("Novo nome de usuário: ")

    if novo_usuario in my_database.database:
        print("Nome de usuário já em uso. Por favor, escolha outro.")
        return

    usar_gerador = input("Deseja usar o gerador de senhas para criar uma senha aleatória? (s/n): ").lower() == 's'

    if usar_gerador:
        comprimento = int(input("Comprimento da senha: "))
        usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
        usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
        usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
        usar_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

        nova_senha = gerar_senha(comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais)
        print("Sua senha gerada:", nova_senha)
    else:
        nova_senha = input("Nova senha: ")

    my_database.database[novo_usuario] = nova_senha
    print("Registro concluído com sucesso!")

def main():
    while True:
        print("\n=== Sistema de Login ===")
        print("1. Fazer Login")
        print("2. Registrar")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            fazer_login()
        elif opcao == '2':
            registrar()
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
