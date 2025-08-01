import string
import random

def gerar_senha(site, semente):
    semente = int(semente) % 1000

    letras = string.ascii_letters
    simbolos = "!@#$%^&*()-_=+[]{};:,.<>?/|\\"
    numeros = string.digits
    alfabeto_louco = letras + numeros + simbolos

    senha_base = ""
    simbolos_usados = 0

    for i, letra in enumerate(site):
        if letra not in alfabeto_louco:
            senha_base += letra
            continue

        idx_original = alfabeto_louco.index(letra)
        idx_novo = (idx_original + semente + i) % len(alfabeto_louco)
        nova_letra = alfabeto_louco[idx_novo]
        senha_base += nova_letra

        # Adiciona símbolo aleatório se ainda não passou de 3
        if simbolos_usados < 3 and random.random() < 0.4:  # 40% de chance
            senha_base += random.choice(simbolos)
            simbolos_usados += 1

    # Garante que a senha tenha pelo menos 1 maiúscula e 1 minúscula
    if not any(c.islower() for c in senha_base):
        senha_base += random.choice(string.ascii_lowercase)

    if not any(c.isupper() for c in senha_base):
        senha_base += random.choice(string.ascii_uppercase)

    # Corta ou preenche a senha para ficar entre 8 e 12 caracteres, sem contar a semente
    if len(senha_base) < 8:
        senha_base += random.choice(letras + numeros) * (8 - len(senha_base))
    elif len(senha_base) > 12:
        senha_base = senha_base[:12]

    # Adiciona a semente no final
    senha_final = senha_base + str(semente)

    return senha_final

# Execução
site = input("Digite o nome do site: ")
semente = input("Digite um número (até 3 dígitos): ")

senha_gerada = gerar_senha(site, semente)
print(f"Senha gerada: {senha_gerada}")
