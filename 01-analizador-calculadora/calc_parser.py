import ply.yacc as yacc
from calc_lexer import tokens
import calc_lexer
import sys

VERBOSE = 1

errores = 0
lineas_error = []
ultimo_token = None
token_anterior = None

def obtener_token():
    global ultimo_token, token_anterior
    tok = calc_lexer.lexer.token()
    if tok is not None:
        token_anterior = ultimo_token
        ultimo_token = tok
    return tok

def p_program(p):
    'program : statement_list'
    pass

def p_statement_list_1(p):
    'statement_list : statement_list statement'
    pass

def p_statement_list_2(p):
    'statement_list : statement'
    pass

def p_statement(p):
    '''statement : let_stmt SEMICOLON
                | assign_stmt SEMICOLON
                | selection_stmt SEMICOLON
                | print_stmt SEMICOLON
                | expression_stmt SEMICOLON
    '''
    pass

def p_statement_error(p):
    'statement : error SEMICOLON'
    p.parser.errok()

def p_let_stmt(p):
    'let_stmt : LET ID EQUAL expression'
    pass

def p_assign_stmt(p):
    'assign_stmt : ID EQUAL expression'
    pass

def p_selection_stmt_1(p):
    'selection_stmt : IF LPAREN expression RPAREN THEN simple_stmt'
    pass

def p_selection_stmt_2(p):
    'selection_stmt : IF LPAREN expression RPAREN THEN simple_stmt ELSE simple_stmt'
    pass

def p_simple_stmt(p):
    '''simple_stmt : assign_stmt
                  | print_stmt
                  | expression_stmt
    '''
    pass

def p_print_stmt(p):
    'print_stmt : PRINT LPAREN expression RPAREN'
    pass

def p_expression_stmt(p):
    'expression_stmt : expression'
    pass

def p_expression_1(p):
    'expression : additive_expression relop additive_expression'
    pass

def p_expression_2(p):
    'expression : additive_expression'
    pass

def p_relop(p):
    '''relop : LESS
            | LESSEQUAL
            | GREATER
            | GREATEREQUAL
            | NOTEQUAL
            | ISEQUAL
    '''
    pass

def p_additive_expression_1(p):
    'additive_expression : additive_expression addop term'
    pass

def p_additive_expression_2(p):
    'additive_expression : term'
    pass

def p_addop(p):
    '''addop : PLUS
            | MINUS
    '''
    pass

def p_term_1(p):
    'term : term mulop power'
    pass

def p_term_2(p):
    'term : power'
    pass

def p_mulop(p):
    '''mulop :     TIMES
                | DIVIDE
                | PERCENT
                | MOD
    '''
    pass

def p_power_1(p):
    'power : factor POWER power'
    pass

def p_power_2(p):
    'power : factor'
    pass

def p_factor_1(p):
    'factor : LPAREN expression RPAREN'
    pass

def p_factor_2(p):
    'factor : ID'
    pass

def p_factor_3(p):
    'factor : call'
    pass

def p_factor_4(p):
    'factor : NUMBER'
    pass

def p_factor_5(p):
    'factor : constant'
    pass

def p_factor_6(p):
    '''factor : MINUS factor
             | NOT factor
    '''
    pass

def p_constant(p):
    '''constant : PI
               | E
               | ANS
    '''
    pass

def p_call(p):
    '''call : SQRT LPAREN expression RPAREN
           | EXP LPAREN expression RPAREN
    '''
    pass


def p_error(p):
    global errores
    errores += 1
    if VERBOSE:
        if p is not None and token_anterior is not None and token_anterior.type != 'SEMICOLON' and token_anterior.lineno < p.lineno:
            lineas_error.append(token_anterior.lineno)
            print ("ERROR SINTACTICO EN LA LINEA " + str(token_anterior.lineno) + " FALTA ; ANTES DEL Token  " + str(p.value))
        elif p is not None:
            lineas_error.append(p.lineno)
            print ("ERROR SINTACTICO EN LA LINEA " + str(p.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
        else:
            if ultimo_token is not None:
                linea = ultimo_token.lineno
            else:
                linea = calc_lexer.lexer.lineno
            lineas_error.append(linea)
            if ultimo_token is not None and ultimo_token.type != 'SEMICOLON':
                print ("ERROR SINTACTICO EN LA LINEA " + str(linea) + " FALTA ; AL FINAL DEL ARCHIVO")
            else:
                print ("ERROR SINTACTICO EN LA LINEA: " + str(linea))
    else:
        raise Exception('syntax', 'error')


parser = yacc.yacc(debug=False, write_tables=False)

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'calculadora.calc'

    f = open(fin, 'r')
    data = f.read()
    #print (data)
    parser.parse(data, lexer=calc_lexer.lexer, tokenfunc=obtener_token, tracking=True)
    if errores == 0 and calc_lexer.errores_lexicos == 0:
        print("Amiguito, tengo el placer de informar que Tu parser reconocio correctamente todo")
    else:
        print("TOTAL DE ERRORES LEXICOS: " + str(calc_lexer.errores_lexicos))
        if calc_lexer.errores_lexicos > 0:
            print("LINEAS CON ERRORES LEXICOS: " + ", ".join(str(l) for l in calc_lexer.lineas_error_lexico))
        print("TOTAL DE ERRORES SINTACTICOS: " + str(errores))
        if errores > 0:
            print("LINEAS CON ERRORES SINTACTICOS: " + ", ".join(str(l) for l in lineas_error))
    #input()
