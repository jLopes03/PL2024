import ply.lex as lex
import re
import sys
import json

tokens = [
    "LISTAR",
    "MOEDA",
    "SELECIONAR",
    "SAIR",
]

def read_json(file_name):
    prod_dict = {}
    with open(file_name,"r") as f:
        prod_list = json.load(f)
        for item in prod_list:
            key = item["cod"]
            prod_dict[key] = item
    return prod_dict


def write_to_json(file_name,prod_dict):
    prod_list = list(prod_dict.values())
    with open(file_name,"w") as f:
        json.dump(prod_list,f,indent=8)

t_LISTAR = r"LISTAR"

t_SAIR = r"SAIR"

def t_MOEDA(t):
    r"MOEDA(?:\s+\d+[ec](?:,|\ \.))+"
    balance = 0
    coins = re.findall(r"\b(\d+)(e|c)\b",t.value)
    for c in coins:
        balance += int(c[0]) if c[1] == "c" else int(c[0]) * 100
    t.value = balance
    return t     

def t_SELECIONAR(t):
    r"SELECIONAR\s+[A-Z]\d+"
    m = re.search(r"\b([A-Z]\d+)\b",t.value)
    t.value = m.group(1)
    return t

t_ignore = " \r\n"

def t_error(t):
    print(f"Unexpected character: {t.value[0]}")
    t.lexer.skip(1)

def main():
    
    prod_dict = read_json("stock.json")
    
    balance = 0
    
    stop = False
    lexer = lex.lex()
    print("maq: Qual é o pedido?")
    while not stop:
        line = input(">")
        lexer.input(line)
        while tok := lexer.token():
            match tok.type:
                case "LISTAR":
                    print("cod   | nome       | quantidade  | preço  \n----------------------------------------")
                    for value in prod_dict.values():
                        print(f'{value["cod"]}     {value["nome"]}    {value["quant"]}             {value["preco"]}  ')
                    
                case "SAIR":                    
                    print("Troco:",balance/100)
                    stop = True

                case "MOEDA":
                    balance += tok.value
                    print("Saldo:",balance/100)

                case "SELECIONAR":
                    prod = prod_dict[tok.value] 
                    if balance < prod["preco"] * 100:
                        print(f'Saldo insuficiente.\nSaldo: {balance/100}. Pedido: {prod["preco"]}')
                    else:
                        balance -= prod["preco"] * 100
                        prod["quant"] -= 1
                        print(f'Pode retirar o produto: {prod["nome"]}\nSaldo restante:{balance/100}')

                case _: 
                    pass

    write_to_json("stock.json",prod_dict)

main()
