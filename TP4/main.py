import ply.lex as lex
import sys

reserved = {
    "select": "SELECT",
    "from": "FROM",
    "where": "WHERE"
}

tokens = [
    "NUMBER",
    "DELIMITER",
    "MATH_SYMBOL",
    "FIELD",
] + list(reserved.values())

t_ignore = " \t\n"

t_DELIMITER = r","

t_MATH_SYMBOL = r"<=|>=|=|<|>"

def t_NUMBER(t): 
    r"[-+]?\d+(?:\.\d+)?"
    t.value = int(t.value) if "." not in t.value else float(t.value)
    return t

def t_FIELD(t):
    r"[a-zA-Z]+"
    t.type = reserved.get(t.value.lower()) if t.value.lower() in reserved else "FIELD"
    return t


def t_error(t):
    print(f"Unexpected character: {t.value[0]}")
    t.lexer.skip(1)

def main(data):
    
    lexer = lex.lex()
    for line in data:
        lexer.input(line)
        while tok := lexer.token():
            print(tok)

main(sys.stdin)