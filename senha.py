# Imprime as regras de validação para criar uma senha.
print("As regras de validação para criar sua conta devem conter o mínimo sugerido:")
print("- Mínimo de 11 e máximo de 18 caracteres;")
print("- Deve ter pelo menos 1 letra minúscula entre [a-z] e 1 letra maiúscula entre [A-Z];")
print("- Deve ter pelo menos 1 número entre [0-9];")
print("- Mínimo de um caractere especial, podendo ser: @_!#$%^&*()<>?/\|}{~:")

import re  # Importa o módulo re (expressões regulares -  (regex))

senha = input("Entre com uma senha: ")

x = True
while x:
    # Verifica se a senha atende aos critérios especificados.
    if (len(senha) < 11 or len(senha) > 19):
        break
    # A função re.search() é utilizada para encontrar um padrão dentro de uma string
    elif not re.search("[a-z]", senha):
        break
    elif not re.search("[0-9]", senha):
        break
    elif not re.search("[A-Z]", senha):
        break
    elif not re.search("[@_!#$%^&*()<>?/\|}{~:]", senha):
        break
    #Verifica se a senha contém espaços em branco, como espaços, tabulações ou quebras de linha.
    elif re.search("\s", senha):
        break
    else:
        print("Senha Válida")
        x = False
        break
        
if x:
    print("Senha inválida")
