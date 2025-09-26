#calculadora hexadecimal

def int_para_hex(num):
    return hex(num)

def hex_para_int(hex_str):
    return int(hex_str, 16)

def mostrar_explicacao():
    print("\n=== COMO FUNCIONA A CONVERSÃO ===\n")
    print("Decimal para Hexadecimal (base 10 → base 16):")
    print("- A base decimal usa potências de 10: 10^0, 10^1, 10^2...")
    print("- A base hexadecimal usa potências de 16: 16^0, 16^1, 16^2...")
    print("- Cada dígito hexadecimal pode ir de 0 até F (F = 15)")
    print("- Exemplo: número 255 em decimal:")
    print("    255 ÷ 16 = 15, resto 15 → F")
    print("    15 ÷ 16 = 0, resto 15 → F")
    print("    Resultado: 0xFF\n")

    print("Hexadecimal para Decimal (base 16 → base 10):")
    print("- Pegue cada dígito da direita para a esquerda e multiplique:")
    print("- Exemplo: 0xFF")
    print("    F = 15 → 15 * 16^0 = 15")
    print("    F = 15 → 15 * 16^1 = 240")
    print("    Soma: 240 + 15 = 255\n")

    print("Prefixo '0x':")
    print("- Em Python, hexadecimais geralmente começam com '0x'.")
    print("- Se digitar sem '0x', o programa adiciona pra você.\n")

print("="*35)
print("       CALCULADORA HEXADECIMAL       ")
print("="*35)

while True:
    print("\nEscolha a operação:")
    print("1. Decimal → Hexadecimal")
    print("2. Hexadecimal → Decimal")
    print("3. Explicação da conversão")
    print("4. Sair")

    opcao = input("Digite a opção (1, 2, 3 ou 4): ")

    if opcao == "1":
        try:
            num = int(input("Digite um número inteiro decimal: "))
            print(f"Hexadecimal: {hex(num)}")
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros.")
    elif opcao == "2":
        hex_str = input("Digite um número hexadecimal (ex: 0xff ou ff): ")
        try:
            if not hex_str.startswith("0x"):
                hex_str = "0x" + hex_str
            print(f"Decimal: {int(hex_str, 16)}")
        except ValueError:
            print("Entrada inválida. Use um valor hexadecimal correto.")
    elif opcao == "3":
        mostrar_explicacao()
    elif opcao == "4":
        print("Encerrando a calculadora. Até logo!")
        break
    else:
        print("Opção inválida. Escolha 1, 2, 3 ou 4.")
