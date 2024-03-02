#aqui vou importar a biblioteca random do python que é util para gerar numeros aleatorios
#tambem estou importando a biblioteca string para fornecer funções e constantes para a manipulação de strings 
import random
import string

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

def main():
    comprimento = int(input("Comprimento da senha: "))
    usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
    usar_especiais = input("Incluir caracteres especiais? (s/n): ").lower() == 's'

    senha = gerar_senha(comprimento, usar_maiusculas, usar_minusculas, usar_numeros, usar_especiais)
    print("Sua senha gerada:", senha)

if __name__ == "__main__":
    main()
