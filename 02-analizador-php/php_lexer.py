import ply.lex as lex
import os
import re
import sys

# lista de tokens
tokens = (
    # etiquetas de apertura y cierre
    'OPEN_TAG',
    'OPEN_TAG_ECHO',
    'CLOSE_TAG',

    # palabras reservadas
    'ABSTRACT',
    'AND',
    'ARRAY',
    'AS',
    'BREAK',
    'CALLABLE',
    'CASE',
    'CATCH',
    'CLASS',
    'CLONE',
    'CONST',
    'CONTINUE',
    'DECLARE',
    'DEFAULT',
    'DO',
    'ECHO',
    'ELSE',
    'ELSEIF',
    'EMPTY',
    'ENDDECLARE',
    'ENDFOR',
    'ENDFOREACH',
    'ENDIF',
    'ENDSWITCH',
    'ENDWHILE',
    'ENUM',
    'EXIT',
    'EXTENDS',
    'FINAL',
    'FINALLY',
    'FN',
    'FOR',
    'FOREACH',
    'FUNCTION',
    'GLOBAL',
    'GOTO',
    'IF',
    'IMPLEMENTS',
    'INCLUDE',
    'INCLUDE_ONCE',
    'INSTANCEOF',
    'INSTEADOF',
    'INTERFACE',
    'ISSET',
    'LIST',
    'MATCH',
    'NAMESPACE',
    'NEW',
    'OR',
    'PRINT',
    'PRIVATE',
    'PROTECTED',
    'PUBLIC',
    'READONLY',
    'REQUIRE',
    'REQUIRE_ONCE',
    'RETURN',
    'STATIC',
    'SWITCH',
    'THROW',
    'TRAIT',
    'TRY',
    'UNSET',
    'USE',
    'VAR',
    'WHILE',
    'XOR',
    'YIELD',
    # constantes
    'TRUE',
    'FALSE',
    'NULL',

    # operadores aritméticos
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULO',
    'POWER',
    'INCREMENT',
    'DECREMENT',
    # operadores de asignación
    'EQUAL',
    'PLUSEQUAL',
    'MINUSEQUAL',
    'TIMESEQUAL',
    'DIVEQUAL',
    'MODEQUAL',
    'POWEREQUAL',
    'CONCATEQUAL',
    'COALESCEEQUAL',
    'ANDEQUAL',
    'OREQUAL',
    'XOREQUAL',
    'SHIFTLEFTEQUAL',
    'SHIFTRIGHTEQUAL',
    # comparación
    'ISEQUAL',
    'IDENTICAL',
    'NOTEQUAL',
    'NOTIDENTICAL',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'SPACESHIP',
    # lógicos
    'LAND',
    'LOR',
    'NOT',
    # bit a bit
    'AMPERSAND',
    'PIPE',
    'CARET',
    'TILDE',
    'SHIFTLEFT',
    'SHIFTRIGHT',
    # otros operadores
    'CONCAT',
    'COALESCE',
    'QUESTION',
    'COLON',
    'ARROW',
    'NULLSAFE_ARROW',
    'DOUBLE_ARROW',
    'DOUBLE_COLON',
    'ELLIPSIS',
    'BACKSLASH',
    'AT',
    # agrupación y puntuación
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'COMMA',

    # otros
    'VARIABLE',
    'ID',
    'INTEGER',
    'FLOAT',
    'STRING',
)

# Regular expressions rules for a simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_MODULO    = r'%'
t_EQUAL     = r'='
t_LESS      = r'<'
t_GREATER   = r'>'
t_NOT       = r'!'
t_AMPERSAND = r'&'
t_PIPE      = r'\|'
t_CARET     = r'\^'
t_TILDE     = r'~'
t_CONCAT    = r'\.'
t_QUESTION  = r'\?'
t_COLON     = r':'
t_BACKSLASH = r'\\'
t_AT        = r'@'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_SEMICOLON = r';'
t_COMMA     = r','

# etiquetas (van primero para que '<?php' no se lea como '<' y '?')
def t_OPEN_TAG(t):
    r'<\?php\b'
    return t

def t_OPEN_TAG_ECHO(t):
    r'<\?='
    return t

def t_CLOSE_TAG(t):
    r'\?>'
    return t

# comentarios (antes de los operadores para que '//' no sea DIVIDE)
def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'//((?!\?>).)*'

def t_comments_shell(t):
    r'\#((?!\?>).)*'

# palabras reservadas (en PHP no distinguen mayúsculas, ver reflags abajo)
def t_ABSTRACT(t):
    r'abstract\b'
    return t

def t_AND(t):
    r'and\b'
    return t

def t_ARRAY(t):
    r'array\b'
    return t

def t_AS(t):
    r'as\b'
    return t

def t_BREAK(t):
    r'break\b'
    return t

def t_CALLABLE(t):
    r'callable\b'
    return t

def t_CASE(t):
    r'case\b'
    return t

def t_CATCH(t):
    r'catch\b'
    return t

def t_CLASS(t):
    r'class\b'
    return t

def t_CLONE(t):
    r'clone\b'
    return t

def t_CONST(t):
    r'const\b'
    return t

def t_CONTINUE(t):
    r'continue\b'
    return t

def t_DECLARE(t):
    r'declare\b'
    return t

def t_DEFAULT(t):
    r'default\b'
    return t

def t_DO(t):
    r'do\b'
    return t

def t_ECHO(t):
    r'echo\b'
    return t

def t_ELSEIF(t):
    r'elseif\b'
    return t

def t_ELSE(t):
    r'else\b'
    return t

def t_EMPTY(t):
    r'empty\b'
    return t

def t_ENDDECLARE(t):
    r'enddeclare\b'
    return t

def t_ENDFOREACH(t):
    r'endforeach\b'
    return t

def t_ENDFOR(t):
    r'endfor\b'
    return t

def t_ENDIF(t):
    r'endif\b'
    return t

def t_ENDSWITCH(t):
    r'endswitch\b'
    return t

def t_ENDWHILE(t):
    r'endwhile\b'
    return t

def t_ENUM(t):
    r'enum\b'
    return t

def t_EXIT(t):
    r'(exit|die)\b'
    return t

def t_EXTENDS(t):
    r'extends\b'
    return t

def t_FINALLY(t):
    r'finally\b'
    return t

def t_FINAL(t):
    r'final\b'
    return t

def t_FN(t):
    r'fn\b'
    return t

def t_FOREACH(t):
    r'foreach\b'
    return t

def t_FOR(t):
    r'for\b'
    return t

def t_FUNCTION(t):
    r'function\b'
    return t

def t_GLOBAL(t):
    r'global\b'
    return t

def t_GOTO(t):
    r'goto\b'
    return t

def t_IF(t):
    r'if\b'
    return t

def t_IMPLEMENTS(t):
    r'implements\b'
    return t

def t_INCLUDE_ONCE(t):
    r'include_once\b'
    return t

def t_INCLUDE(t):
    r'include\b'
    return t

def t_INSTANCEOF(t):
    r'instanceof\b'
    return t

def t_INSTEADOF(t):
    r'insteadof\b'
    return t

def t_INTERFACE(t):
    r'interface\b'
    return t

def t_ISSET(t):
    r'isset\b'
    return t

def t_LIST(t):
    r'list\b'
    return t

def t_MATCH(t):
    r'match\b'
    return t

def t_NAMESPACE(t):
    r'namespace\b'
    return t

def t_NEW(t):
    r'new\b'
    return t

def t_OR(t):
    r'or\b'
    return t

def t_PRINT(t):
    r'print\b'
    return t

def t_PRIVATE(t):
    r'private\b'
    return t

def t_PROTECTED(t):
    r'protected\b'
    return t

def t_PUBLIC(t):
    r'public\b'
    return t

def t_READONLY(t):
    r'readonly\b'
    return t

def t_REQUIRE_ONCE(t):
    r'require_once\b'
    return t

def t_REQUIRE(t):
    r'require\b'
    return t

def t_RETURN(t):
    r'return\b'
    return t

def t_STATIC(t):
    r'static\b'
    return t

def t_SWITCH(t):
    r'switch\b'
    return t

def t_THROW(t):
    r'throw\b'
    return t

def t_TRAIT(t):
    r'trait\b'
    return t

def t_TRY(t):
    r'try\b'
    return t

def t_UNSET(t):
    r'unset\b'
    return t

def t_USE(t):
    r'use\b'
    return t

def t_VAR(t):
    r'var\b'
    return t

def t_WHILE(t):
    r'while\b'
    return t

def t_XOR(t):
    r'xor\b'
    return t

def t_YIELD(t):
    r'yield\b'
    return t

def t_TRUE(t):
    r'true\b'
    return t

def t_FALSE(t):
    r'false\b'
    return t

def t_NULL(t):
    r'null\b'
    return t

# variables: $nombre
def t_bad_VARIABLE(t):
    r'\$\d[a-zA-Z0-9_]*'
    print ("Lexical error: variable invalida '" + t.value + "' en linea " + str(t.lexer.lineno))

def t_VARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# cadenas con comillas simples y dobles
def t_STRING(t):
    r'\'([^\'\\]|\\(.|\n))*\'|"([^"\\]|\\(.|\n))*"'
    t.lexer.lineno += t.value.count('\n')
    return t

# números (FLOAT antes que INTEGER para que 3.14 no se parta)
def t_FLOAT(t):
    r'(\d[\d_]*)?\.\d[\d_]*([eE][+-]?\d+)?|\d[\d_]*[eE][+-]?\d+'
    t.value = float(t.value.replace('_', ''))
    return t

def t_bad_ID(t):
    r'(?!0[xXbBoO])\d[\d_]*[a-zA-Z][a-zA-Z0-9_]*'
    print ("Lexical error: identificador invalido '" + t.value + "' en linea " + str(t.lexer.lineno))

def t_INTEGER(t):
    r'0[xX][0-9a-fA-F_]+|0[bB][01_]+|0[oO][0-7_]+|\d[\d_]*'
    t.value = int(t.value.replace('_', ''), 0) if t.value[:2].lower() in ('0x', '0b', '0o') else int(t.value.replace('_', ''))
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# operadores de varios caracteres (de mayor a menor longitud)
def t_POWEREQUAL(t):
    r'\*\*='
    return t

def t_COALESCEEQUAL(t):
    r'\?\?='
    return t

def t_SHIFTLEFTEQUAL(t):
    r'<<='
    return t

def t_SHIFTRIGHTEQUAL(t):
    r'>>='
    return t

def t_IDENTICAL(t):
    r'==='
    return t

def t_NOTIDENTICAL(t):
    r'!=='
    return t

def t_SPACESHIP(t):
    r'<=>'
    return t

def t_ELLIPSIS(t):
    r'\.\.\.'
    return t

def t_NULLSAFE_ARROW(t):
    r'\?->'
    return t

def t_POWER(t):
    r'\*\*'
    return t

def t_INCREMENT(t):
    r'\+\+'
    return t

def t_DECREMENT(t):
    r'--'
    return t

def t_PLUSEQUAL(t):
    r'\+='
    return t

def t_MINUSEQUAL(t):
    r'-='
    return t

def t_TIMESEQUAL(t):
    r'\*='
    return t

def t_DIVEQUAL(t):
    r'/='
    return t

def t_MODEQUAL(t):
    r'%='
    return t

def t_CONCATEQUAL(t):
    r'\.='
    return t

def t_ANDEQUAL(t):
    r'&='
    return t

def t_OREQUAL(t):
    r'\|='
    return t

def t_XOREQUAL(t):
    r'\^='
    return t

def t_ISEQUAL(t):
    r'=='
    return t

def t_NOTEQUAL(t):
    r'!=|<>'
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_SHIFTLEFT(t):
    r'<<'
    return t

def t_SHIFTRIGHT(t):
    r'>>'
    return t

def t_LAND(t):
    r'&&'
    return t

def t_LOR(t):
    r'\|\|'
    return t

def t_COALESCE(t):
    r'\?\?'
    return t

def t_ARROW(t):
    r'->'
    return t

def t_DOUBLE_ARROW(t):
    r'=>'
    return t

def t_DOUBLE_COLON(t):
    r'::'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t\r'

def t_error(t):
    print ("Lexical error: '" + str(t.value[0]) + "' en linea " + str(t.lexer.lineno))
    t.lexer.skip(1)

def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

# las palabras reservadas de PHP no distinguen mayúsculas (IF, If, if)
lexer = lex.lex(reflags=int(re.VERBOSE | re.IGNORECASE))


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        # se busca junto al script, sin importar desde dónde se ejecute
        fin = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'programa.php')
    f = open(fin, 'r')
    data = f.read()
    print (data)
    lexer.input(data)
    test(data, lexer)
    #input()
