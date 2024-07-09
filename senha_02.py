import re

# Define uma expressão regular para verificar a presença de caracteres especiais na senha.
caractere_especial = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')

print("Sua Senha deve conter o mínimo sugerido:")
print("Mínimo 11 dígitos")
print("Pelo menos um número e uma letra")
print("Qualquer letra de a a z")
print("Qualquer número de 0 a 9")
print("Pelo menos uma letra maiúscula e uma minúscula")
print("Mínimo de um caractere especial, podendo ser: @_!#$%^&*()<>?/\|}{~:")

senha = input("Digite sua senha: ")

# Conta o número de dígitos na senha.
num_digitos = sum(c.isdigit() for c in senha)

# Verifica se a senha atende aos critérios especificados.
if (len(senha) >= 11 and
    any(c.isupper() for c in senha) and
    any(c.islower() for c in senha) and
    num_digitos >= 1 and
    caractere_especial.search(senha) is not None):
    print("Senha válida!")
else:
    print("A senha não atende aos critérios especificados.")

