# Analizador léxico de PHP

Analizador léxico para PHP

## Output del programa

```
<?php
// Función sin parámetros ni retorno
function mostrarSaludo() {
    echo "¡Hola, bienvenido a PHP!<br>";
}

// Función con parámetros y valor de retorno (return)
function sumarNumeros($num1, $num2) {
    $8 = 5x + $num2;
    return $resultado;
}

// Invocación de las funciones
mostrarSaludo(); // Muestra el saludo

$total = sumarNumeros(5, 10); // Guarda el valor retornado
echo "La suma es: " . $total;
?>
LexToken(OPEN_TAG,'<?php',1,0)
LexToken(FUNCTION,'function',3,43)
LexToken(ID,'mostrarSaludo',3,52)
LexToken(LPAREN,'(',3,65)
LexToken(RPAREN,')',3,66)
LexToken(LBRACE,'{',3,68)
LexToken(ECHO,'echo',4,74)
LexToken(STRING,'"¡Hola, bienvenido a PHP!<br>"',4,79)
LexToken(SEMICOLON,';',4,109)
LexToken(RBRACE,'}',5,111)
LexToken(FUNCTION,'function',8,168)
LexToken(ID,'sumarNumeros',8,177)
LexToken(LPAREN,'(',8,189)
LexToken(VARIABLE,'$num1',8,190)
LexToken(COMMA,',',8,195)
LexToken(VARIABLE,'$num2',8,197)
LexToken(RPAREN,')',8,202)
LexToken(LBRACE,'{',8,204)
Lexical error: variable invalida '$8' en linea 9
LexToken(EQUAL,'=',9,213)
Lexical error: identificador invalido '5x' en linea 9
LexToken(PLUS,'+',9,218)
LexToken(VARIABLE,'$num2',9,220)
LexToken(SEMICOLON,';',9,225)
LexToken(RETURN,'return',10,231)
LexToken(VARIABLE,'$resultado',10,238)
LexToken(SEMICOLON,';',10,248)
LexToken(RBRACE,'}',11,250)
LexToken(ID,'mostrarSaludo',14,284)
LexToken(LPAREN,'(',14,297)
LexToken(RPAREN,')',14,298)
LexToken(SEMICOLON,';',14,299)
LexToken(VARIABLE,'$total',16,323)
LexToken(EQUAL,'=',16,330)
LexToken(ID,'sumarNumeros',16,332)
LexToken(LPAREN,'(',16,344)
LexToken(INTEGER,5,16,345)
LexToken(COMMA,',',16,346)
LexToken(INTEGER,10,16,348)
LexToken(RPAREN,')',16,350)
LexToken(SEMICOLON,';',16,351)
LexToken(ECHO,'echo',17,382)
LexToken(STRING,'"La suma es: "',17,387)
LexToken(CONCAT,'.',17,402)
LexToken(VARIABLE,'$total',17,404)
LexToken(SEMICOLON,';',17,410)
LexToken(CLOSE_TAG,'?>',18,412)
```
