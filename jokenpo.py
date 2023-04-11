from movimentos import dicionarioDecisao
import random


def main():
    decisaoUsuario = input("Você escolhe pedra, papel ou tesoura? ")
    decisaoPC = random.choice(["pedra", "papel", "tesoura"])

    print(f"Sua escolha: {dicionarioDecisao[decisaoUsuario]}")
    print(f"Escolha do computador:\n{dicionarioDecisao[decisaoPC]}")

    if decisaoUsuario == decisaoPC:
        print("Empate.")
    elif (decisaoUsuario == "papel" and decisaoPC == "pedra") \
            or (decisaoUsuario == "pedra" and decisaoPC == "tesoura") \
            or (decisaoUsuario == "tesoura" and decisaoPC == "papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu...")


if __name__ == "__main__":
    main()
