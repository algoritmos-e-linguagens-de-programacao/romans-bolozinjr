def int_to_roman(num):
    decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // decimal[i]):
            roman_num += romanos[i]
            num -= decimal[i]
        i += 1
    return roman_num

def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_num = 0
    prev_value = 0
    for char in s:
        value = roman_dict[char]
        if value > prev_value:
            integer_num += value - 2 * prev_value
        else:
            integer_num += value
        prev_value = value
    return integer_num

# def main():
#     while True:
#         choice = input("Digite '1' para converter um número inteiro para romano, ou '2' para converter um número romano para inteiro, ou 'sair' para encerrar: ")
        
#         if choice == '1':
#             num = int(input("Digite um número inteiro: "))
#             print("Número romano correspondente:", int_to_roman(num))
#         elif choice == '2':
#             num = input("Digite um número romano: ")
#             print("Número inteiro correspondente:", roman_to_int(num))
#         elif choice.lower() == 'sair':
#             print("Programa encerrado.")
#             break
#         else:
#             print("Escolha inválida. Tente novamente.")

# if __name__ == "__main__":
#     main()
