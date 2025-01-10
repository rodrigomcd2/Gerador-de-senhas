import secrets
import string

try:
    tamanho_da_senha = int(input("Tamanho da senha (no mínimo 8 caracteres): "))
    if tamanho_da_senha < 8:
        raise ValueError("O comprimento da senha deve ser no mínimo 8 caracteres.")
except ValueError as e:
    print(e)
    exit()

alphabet = string.ascii_letters + string.digits
senha = ''.join(secrets.choice(alphabet) for _ in range(tamanho_da_senha))

print("Sua senha gerada é:", senha)
