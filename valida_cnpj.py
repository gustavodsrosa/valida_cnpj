# Módulo para remover pontos e barras do CNPJ
import re

# Removendo caracteres indesejáveis


def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


# Adicionando um CNPJ sem dígitos, para iniciar a validação
# cnpj = str(input("Digite um CNPJ para obter os dígitos: "))

# Exemplo de CNPJ:
cnpj = '71.506.168/0001'
cnpj_clean = remover_caracteres(cnpj)

# Converter cada índice da minha lista em inteiro
cnpj_clean = list(map(int, cnpj_clean))


def encontrar_primeiro_digito():

    # Algoritmo usado para verificar dígito final
    template = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    # List Comprehension que faz o incremento dos valores
    soma = sum(template[i] * cnpj_clean[i] for i in range(len(template)))

    # Algoritmo para se realizar o cálculo da fórmula
    resultado_formula = 11 - (soma % 11)

    if resultado_formula > 9:
        primeiro_digito = 0
        cnpj_clean.append(primeiro_digito)
    else:
        primeiro_digito = resultado_formula
        cnpj_clean.append(primeiro_digito)


def encontrar_segundo_digito():

    template2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    soma2 = sum(template2[i] * cnpj_clean[i] for i in range(len(template2)))

    resultado_formula_segundo = 11 - (soma2 % 11)

    if resultado_formula_segundo > 9:
        segundo_digito = 0
        cnpj_clean.append(segundo_digito)
    else:
        segundo_digito = resultado_formula_segundo
        cnpj_clean.append(segundo_digito)


# Chamando as funções
encontrar_primeiro_digito()
encontrar_segundo_digito()

# Imprimir valores da lista para se mostrar o CNPJ
print()
for a in range(len(cnpj_clean)):
    print(cnpj_clean[a], end='')
print()
