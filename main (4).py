import pickle
import os
import pprint
from datetime import datetime

# ==============================
# FUNÇÃO PARA FORMATAR DATA
# ==============================
def formata_data():
    while True:
        data = input("Digite a data (dd/mm/aaaa): ")
        try:
            data_formatada = datetime.strptime(data, "%d/%m/%Y")
            return data_formatada.strftime("%d/%m/%Y")
        except ValueError:
            print("Data inválida! Use o formato dd/mm/aaaa.\n")

# ==============================
# FUNÇÕES ENTRADAS
# ==============================
def f_entradas(entradas):
    print('ENTRADAS')
    sair = ""
    menu = '''
Escolha uma Opção:
 __________________
|_____Entradas_____| 
|1-Visualizar      |
|2-Adicionar       |
|3-Voltar          |
|__________________|\n
'''
    opt = input(menu)
    while opt != "3":
        if opt == "1":
            os.system("cls")
            while sair != "1":
                mostra_entradas(entradas)
                sair = input("Digite 1 Para voltar: ")
                os.system("cls")

        elif opt == "2":
            os.system("cls")
            add_entrada(entradas)

        sair = ""
        opt = input(menu)

    os.system("cls")


def mostra_entradas(entradas):
    total = 0.0
    os.system("cls")
    for categoria in entradas:
        print(f"Categoria: {categoria}")
        for (data, nome, valor) in entradas[categoria]:
            print(f"({data}) {nome} | Valor: R${valor}")
            total += valor
        print("-------------------------------------")
    print(f"Total das entradas: {total}\n")


def add_entrada(entradas):
    categoria = input("Digite a categoria da entrada (letras minusculas e sem acento):\n")
    data = formata_data()
    nome = input("Digite o nome da entrada:\n")
    valor = float(input("Digite o valor da entrada:\n"))

    os.system("cls")
    print("Entrada Adicionada!")

    if categoria in entradas:
        entradas[categoria].append((data, nome, valor))
    else:
        entradas[categoria] = [(data, nome, valor)]


# ==============================
# FUNÇÕES DESPESAS
# ==============================
def f_despesas(despesas):
    print('Despesas')
    sair = ""
    menu = '''
Escolha uma Opção:
 __________________
|_____Despesas_____| 
|1-Visualizar      |
|2-Adicionar       |
|3-Voltar          |
|__________________|\n
'''
    opt = input(menu)
    while opt != "3":
        if opt == "1":
            os.system("cls")
            while sair != "1":
                mostra_despesas(despesas)
                sair = input("Digite 1 Para voltar: ")
                os.system("cls")

        elif opt == "2":
            os.system("cls")
            add_despesas(despesas)

        sair = ""
        opt = input(menu)

    os.system("cls")


def mostra_despesas(despesas):
    total = 0.0
    os.system("cls")
    for categoria in despesas:
        print(f"Categoria: {categoria}")
        for (data, nome, valor) in despesas[categoria]:
            print(f"({data}) {nome} | Valor: R${valor}")
            total += valor
        print("-------------------------------------")
    print(f"Total das despesas: {total}\n")


def add_despesas(despesas):
    categoria = input("Digite a categoria da despesa (letras minusculas e sem acento):\n")
    data = formata_data()
    nome = input("Digite o nome da despesa:\n")
    valor = float(input("Digite o valor da despesa:\n"))

    os.system("cls")
    print("Despesa Adicionada!")

    if categoria in despesas:
        despesas[categoria].append((data, nome, valor))
    else:
        despesas[categoria] = [(data, nome, valor)]


# ==============================
# FUNÇÕES INVESTIMENTOS
# ==============================
def f_investimentos(investimentos):
    print('Investimentos')
    sair = ""
    menu = '''
Escolha uma Opção:
 __________________
|___Investimentos__|
|1-Visualizar      |
|2-Adicionar       |
|3-Voltar          |
|__________________|\n
'''
    opt = input(menu)
    while opt != "3":
        if opt == "1":
            os.system("cls")
            while sair != "1":
                mostra_investimentos(investimentos)
                sair = input("Digite 1 Para voltar: ")
                os.system("cls")

        elif opt == "2":
            os.system("cls")
            add_investimentos(investimentos)

        sair = ""
        opt = input(menu)

    os.system("cls")


def mostra_investimentos(investimentos):
    total = 0.0
    os.system("cls")
    for categoria in investimentos:
        print(f"Categoria: {categoria}")
        for (data, nome, valor) in investimentos[categoria]:
            print(f"({data}) {nome} | Valor: R${valor}")
            total += valor
        print("-------------------------------------")
    print(f"Total dos investimentos: {total}\n")


def add_investimentos(investimentos):
    categoria = input("Digite a categoria do investimento (letras minusculas e sem acento):\n")
    data = formata_data()
    nome = input("Digite o nome do investimento:\n")
    valor = float(input("Digite o valor do investimento:\n"))

    os.system("cls")
    print("Investimento Adicionado!")

    if categoria in investimentos:
        investimentos[categoria].append((data, nome, valor))
    else:
        investimentos[categoria] = [(data, nome, valor)]


# ==============================
# SALDO FINAL
# ==============================
def calc_total(entradas,despesas,investimentos):
    totalE,totalI,totalD,final=0.00,0.00,0.00,0.00
    for categoria in entradas:
        for (_, _, valor) in entradas[categoria]:
            totalE += valor

    for categoria in despesas:
        for (_, _, valor) in despesas[categoria]:
            totalD += valor

    for categoria in investimentos:
        for (_, _, valor) in investimentos[categoria]:
            totalI += valor

    final = totalE - totalD
    
    return totalE,totalI,totalD,final
def saldo_final(entradas, despesas, investimentos):
    sair = ""

    totalE,totalI,totalD,final=calc_total(entradas,despesas,investimentos)
    
    while sair != "1":
        print("=" * 60)
        print(f"{'RESUMO MENSAL':^60}")
        print("=" * 60)

        print(f"{'Entradas':<25}R${totalE:>12.2f}")
        print(f"{'Despesas':<25}R${totalD:>12.2f}")
        print(f"{'Investimentos':<25}R${totalI:>12.2f}")

        print("-" * 60)
        print(f"{'SALDO FINAL':<25}R${final:>12.2f}")
        print("=" * 60)

        sair = input("1- Voltar")


# ==============================
# ANUAL
# ==============================

def fechamento(meses,entradas,despesas,investimentos,):
    
    totalE,totalI,totalD,final=calc_total(entradas,despesas,investimentos)
    menu='''
Selecione o mês para fazer o fechamento: 
 ___________
|___Meses___|
|1-Janeiro  |
|2-Fevereiro|
|3-Março    |
|4-Abril    |
|5-Maio     |
|6-Junho    |
|7-Julho    |
|8-Agosto   |
|9-Setembro |
|10-Outubro |
|11-Novembro|
|12-Dezembro|
|___________|
'''
    opt=int(input(menu))
    

    #Entradas
    meses[opt][1][0]=totalE
    #saidas
    meses[opt][1][1]=totalD
    #investimentos
    meses[opt][1][2]=totalI
    #SaldoFinal
    meses[opt][1][3]=final
    
    #Zerando os dicionarios
    entradas.clear()
    despesas.clear()
    investimentos.clear()
    
def saida_anual(meses):
    
    os.system("cls")

    print("=" * 95)
    print(f"{'PLANEJAMENTO ANUAL':^95}")
    print("=" * 95)

    # Cabeçalho
    print(f"{'Mês':<15}"
          f"{'Entradas':>15}"
          f"{'Saídas':>15}"
          f"{'Investimentos':>18}"
          f"{'Saldo Final':>15}")
    print("-" * 95)

    # Corpo da tabela
    for i in range(1, 13):
        nome_mes = meses[i][0]
        entradas = meses[i][1][0]
        saidas = meses[i][1][1]
        investimentos = meses[i][1][2]
        saldo = meses[i][1][3]

        print(f"{nome_mes:<15}"
              f"R${entradas:>13.2f}"
              f"R${saidas:>13.2f}"
              f"R${investimentos:>16.2f}"
              f"R${saldo:>13.2f}")

    print("=" * 95)

   
    
def resumo_anual(meses):
    
    sair=''
    while sair!="1":
        saida_anual(meses)
        sair=input("Digite 1 para sair:\n")   
    


# ==============================
# MAIN
# ==============================
def main():
    os.system("cls")

    entradas = {}
    despesas = {}
    investimentos = {}

    menu = '''

Escolha uma Opção:
 __________________
|____Financeiro____|
|1-Entradas        |
|2-Despesas        |
|3-Investimentos   |
|4-Saldo Final     |
|5-Fechar Mês      |
|6-Resumo Anual    |
|7-Sair            |
|__________________|\n
'''

    opt = input(menu)
    while opt != "7":
        if opt == "1":
            os.system("cls")
            f_entradas(entradas)
        elif opt == "2":
            os.system("cls")
            f_despesas(despesas)
        elif opt == "3":
            os.system("cls")
            f_investimentos(investimentos)
        elif opt == "4":
            os.system("cls")
            saldo_final(entradas, despesas, investimentos)

        opt = input(menu)


if __name__ == "__main__":
    main()
