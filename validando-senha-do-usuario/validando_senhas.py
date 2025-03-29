import random
import string

def gerar_senha (tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))  
    return senha

flag = False

def verificar_senha(senha):

    tamanho_senha = len(senha)
    senha_minuscula = not any(char.islower() for char in senha)
    senha_maiuscula = not any(char.isupper() for char in senha)
    senha_digito = not any(char.isdigit() for char in senha)
    senha_caract_especial = not any(char in string.punctuation for char in senha)
 
    if tamanho_senha < 8:
        print('Sua senha tem menos de 8 caracteres.')
    if senha_minuscula:
        print('Sua senha deve conter pelo menos uma letra minúscula.')
    if senha_maiuscula:
        print('Sua senha deve conter pelo menos uma letra maiúscula.')
    if senha_digito:
        print('Sua senha deve conter pelo menos um número.')
    if senha_caract_especial:
        print('Sua senha deve conter pelo menos um caractere especial.')
    if tamanho_senha >= 8 and not senha_minuscula and not senha_maiuscula and not senha_digito and not senha_caract_especial:
        return True
    return flag

while True:
    senha = input('Digite uma senha: ')
    if verificar_senha(senha):
        print('Sua senha é forte')
        break
    else:
        print('Sua senha é fraca. Tente novamente.')