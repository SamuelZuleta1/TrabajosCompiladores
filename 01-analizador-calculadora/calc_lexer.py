import ply.lex as lex
import sys

errores_lexicos = 0
lineas_error_lexico = []

tokens = (
    'SQRT',
    'EXP',
    'PI',
    'E',
    'ANS',
    'LET',
    'MOD',
    'IF',
    'THEN',
    'ELSE',
    'PRINT',

    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'POWER',
    'PERCENT',
    'EQUAL',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'NOTEQUAL',
    'ISEQUAL',
    'NOT',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',

    'ID',
    'NUMBER',
)

t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_POWER     = r'\^'
t_PERCENT   = r'%'
t_EQUAL     = r'='
t_LESS      = r'<'
t_GREATER   = r'>'
t_NOT       = r'!'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_SEMICOLON = r';'

def t_SQRT(t):
    r'sqrt\b'
    return t

def t_EXP(t):
    r'exp\b'
    return t

def t_PI(t):
    r'pi\b'
    return t

def t_ANS(t):
    r'ans\b'
    return t

def t_LET(t):
    r'let\b'
    return t

def t_MOD(t):
    r'mod\b'
    return t

def t_IF(t):
    r'if\b'
    return t

def t_THEN(t):
    r'then\b'
    return t

def t_ELSE(t):
    r'else\b'
    return t

def t_PRINT(t):
    r'print\b'
    return t

def t_E(t):
    r'e\b'
    return t

def t_bad_ID(t):
    r'\d+[a-zA-Z_][a-zA-Z0-9_]*'
    global errores_lexicos
    errores_lexicos += 1
    lineas_error_lexico.append(t.lexer.lineno)
    print ("Lexical error: identificador invalido '" + t.value + "' en linea " + str(t.lexer.lineno))

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_NOTEQUAL(t):
    r'!='
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//.*'

def t_error(t):
    global errores_lexicos
    errores_lexicos += 1
    lineas_error_lexico.append(t.lexer.lineno)
    print ("Lexical error: '" + str(t.value[0]) + "' en linea " + str(t.lexer.lineno))
    t.lexer.skip(1)

def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

lexer = lex.lex()


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'calculadora.calc'
    f = open(fin, 'r')
    data = f.read()
    print (data)
    lexer.input(data)
    test(data, lexer)