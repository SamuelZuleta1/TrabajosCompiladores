# Analizador léxico de PHP

Analizador léxico para PHP

Reconoce:

- **Etiquetas**: `<?php`, `<?=`, `?>`
- **Palabras reservadas** de PHP (`abstract`, `class`, `function`, `if`, `elseif`, `foreach`, `match`, `fn`, `try`, `catch`, `namespace`, `use`, etc.) sin distinguir mayúsculas, como en PHP (`IF`, `If` e `if` son el mismo token)
- **Constantes**: `true`, `false`, `null`
- **Variables** (`$nombre`) e **identificadores**
- **Números**: enteros decimales, hexadecimales (`0x1F`), binarios (`0b1010`), octales (`0o17`), con separador `_` (`1_000`), y reales (`3.14`, `.5`, `1.5e3`)
- **Cadenas** con comillas simples y dobles
- **Operadores** aritméticos, de asignación, comparación (`===`, `!==`, `<=>`), lógicos, bit a bit, `??`, `??=`, `->`, `?->`, `=>`, `::`, `...`
- **Comentarios** `//`, `#` y `/* */`
- **Errores léxicos**: variables inválidas (`$1malo`), identificadores inválidos (`9abc`) y caracteres desconocidos

## Uso

```
python3 php_lexer.py              # analiza programa.php
python3 php_lexer.py archivo.php  # analiza otro archivo
```

## Output del programa

```
<?php
namespace App\Modelos;

use App\Base\Entidad;

/* Clase de ejemplo con propiedades,
   constructor y metodos */
abstract class Figura extends Entidad implements Medible
{
    const LADOS = 0;
    protected static $contador = 0;
    private ?string $nombre = null;

    public function __construct(string $nombre)
    {
        $this->nombre = $nombre;
        self::$contador++;
    }

    abstract public function area(): float;
}

// Variables y tipos de literales
$entero = 42;
$hexa = 0x1F;
$binario = 0b1010;
$real = 3.14;
$cientifico = 1.5e3;
$saludo = 'Hola';
$mensaje = "Mundo\n";
$activo = true;
$vacio = NULL;

# Operadores aritmeticos y de asignacion
$suma = $entero + $real * 2 - 10 / 5 % 3;
$potencia = 2 ** 8;
$entero += 1;
$entero -= 1;
$saludo .= " " . $mensaje;
$vacio ??= 'defecto';

// Comparaciones y logicos
if ($entero === 42 && $real != 0 || !$activo) {
    echo "Iguales";
} elseif ($entero <=> $real) {
    print("Distintos");
} else {
    $resultado = $entero >= 10 ? 'grande' : 'pequeno';
}

// Ciclos
for ($i = 0; $i < 10; $i++) {
    if ($i == 5) continue;
    if ($i <= 8) break;
}

$lista = [1, 2, 3];
foreach ($lista as $clave => $valor) {
    $total = $valor ?? 0;
}

while ($entero > 0) {
    $entero--;
}

// Funciones y excepciones
function sumar(int ...$numeros): int
{
    return array_sum($numeros);
}

try {
    $obj = new Cuadrado(4);
    $area = $obj?->area();
} catch (Exception $e) {
    throw $e;
} finally {
    unset($obj);
}

$doble = fn($x) => $x * 2;

// Errores lexicos
$1malo = 5;
$x = 9abc;
$y = 7 ` 2;
?>

LexToken(OPEN_TAG,'<?php',1,0)
LexToken(NAMESPACE,'namespace',2,6)
LexToken(ID,'App',2,16)
LexToken(BACKSLASH,'\\',2,19)
LexToken(ID,'Modelos',2,20)
LexToken(SEMICOLON,';',2,27)
LexToken(USE,'use',4,30)
LexToken(ID,'App',4,34)
LexToken(BACKSLASH,'\\',4,37)
LexToken(ID,'Base',4,38)
LexToken(BACKSLASH,'\\',4,42)
LexToken(ID,'Entidad',4,43)
LexToken(SEMICOLON,';',4,50)
LexToken(ABSTRACT,'abstract',8,118)
LexToken(CLASS,'class',8,127)
LexToken(ID,'Figura',8,133)
LexToken(EXTENDS,'extends',8,140)
LexToken(ID,'Entidad',8,148)
LexToken(IMPLEMENTS,'implements',8,156)
LexToken(ID,'Medible',8,167)
LexToken(LBRACE,'{',9,175)
LexToken(CONST,'const',10,181)
LexToken(ID,'LADOS',10,187)
LexToken(EQUAL,'=',10,193)
LexToken(INTEGER,0,10,195)
LexToken(SEMICOLON,';',10,196)
LexToken(PROTECTED,'protected',11,202)
LexToken(STATIC,'static',11,212)
LexToken(VARIABLE,'$contador',11,219)
LexToken(EQUAL,'=',11,229)
LexToken(INTEGER,0,11,231)
LexToken(SEMICOLON,';',11,232)
LexToken(PRIVATE,'private',12,238)
LexToken(QUESTION,'?',12,246)
LexToken(ID,'string',12,247)
LexToken(VARIABLE,'$nombre',12,254)
LexToken(EQUAL,'=',12,262)
LexToken(NULL,'null',12,264)
LexToken(SEMICOLON,';',12,268)
LexToken(PUBLIC,'public',14,275)
LexToken(FUNCTION,'function',14,282)
LexToken(ID,'__construct',14,291)
LexToken(LPAREN,'(',14,302)
LexToken(ID,'string',14,303)
LexToken(VARIABLE,'$nombre',14,310)
LexToken(RPAREN,')',14,317)
LexToken(LBRACE,'{',15,323)
LexToken(VARIABLE,'$this',16,333)
LexToken(ARROW,'->',16,338)
LexToken(ID,'nombre',16,340)
LexToken(EQUAL,'=',16,347)
LexToken(VARIABLE,'$nombre',16,349)
LexToken(SEMICOLON,';',16,356)
LexToken(ID,'self',17,366)
LexToken(DOUBLE_COLON,'::',17,370)
LexToken(VARIABLE,'$contador',17,372)
LexToken(INCREMENT,'++',17,381)
LexToken(SEMICOLON,';',17,383)
LexToken(RBRACE,'}',18,389)
LexToken(ABSTRACT,'abstract',20,396)
LexToken(PUBLIC,'public',20,405)
LexToken(FUNCTION,'function',20,412)
LexToken(ID,'area',20,421)
LexToken(LPAREN,'(',20,425)
LexToken(RPAREN,')',20,426)
LexToken(COLON,':',20,427)
LexToken(ID,'float',20,429)
LexToken(SEMICOLON,';',20,434)
LexToken(RBRACE,'}',21,436)
LexToken(VARIABLE,'$entero',24,473)
LexToken(EQUAL,'=',24,481)
LexToken(INTEGER,42,24,483)
LexToken(SEMICOLON,';',24,485)
LexToken(VARIABLE,'$hexa',25,487)
LexToken(EQUAL,'=',25,493)
LexToken(INTEGER,31,25,495)
LexToken(SEMICOLON,';',25,499)
LexToken(VARIABLE,'$binario',26,501)
LexToken(EQUAL,'=',26,510)
LexToken(INTEGER,10,26,512)
LexToken(SEMICOLON,';',26,518)
LexToken(VARIABLE,'$real',27,520)
LexToken(EQUAL,'=',27,526)
LexToken(FLOAT,3.14,27,528)
LexToken(SEMICOLON,';',27,532)
LexToken(VARIABLE,'$cientifico',28,534)
LexToken(EQUAL,'=',28,546)
LexToken(FLOAT,1500.0,28,548)
LexToken(SEMICOLON,';',28,553)
LexToken(VARIABLE,'$saludo',29,555)
LexToken(EQUAL,'=',29,563)
LexToken(STRING,"'Hola'",29,565)
LexToken(SEMICOLON,';',29,571)
LexToken(VARIABLE,'$mensaje',30,573)
LexToken(EQUAL,'=',30,582)
LexToken(STRING,'"Mundo\\n"',30,584)
LexToken(SEMICOLON,';',30,593)
LexToken(VARIABLE,'$activo',31,595)
LexToken(EQUAL,'=',31,603)
LexToken(TRUE,'true',31,605)
LexToken(SEMICOLON,';',31,609)
LexToken(VARIABLE,'$vacio',32,611)
LexToken(EQUAL,'=',32,618)
LexToken(NULL,'NULL',32,620)
LexToken(SEMICOLON,';',32,624)
LexToken(VARIABLE,'$suma',35,668)
LexToken(EQUAL,'=',35,674)
LexToken(VARIABLE,'$entero',35,676)
LexToken(PLUS,'+',35,684)
LexToken(VARIABLE,'$real',35,686)
LexToken(TIMES,'*',35,692)
LexToken(INTEGER,2,35,694)
LexToken(MINUS,'-',35,696)
LexToken(INTEGER,10,35,698)
LexToken(DIVIDE,'/',35,701)
LexToken(INTEGER,5,35,703)
LexToken(MODULO,'%',35,705)
LexToken(INTEGER,3,35,707)
LexToken(SEMICOLON,';',35,708)
LexToken(VARIABLE,'$potencia',36,710)
LexToken(EQUAL,'=',36,720)
LexToken(INTEGER,2,36,722)
LexToken(POWER,'**',36,724)
LexToken(INTEGER,8,36,727)
LexToken(SEMICOLON,';',36,728)
LexToken(VARIABLE,'$entero',37,730)
LexToken(PLUSEQUAL,'+=',37,738)
LexToken(INTEGER,1,37,741)
LexToken(SEMICOLON,';',37,742)
LexToken(VARIABLE,'$entero',38,744)
LexToken(MINUSEQUAL,'-=',38,752)
LexToken(INTEGER,1,38,755)
LexToken(SEMICOLON,';',38,756)
LexToken(VARIABLE,'$saludo',39,758)
LexToken(CONCATEQUAL,'.=',39,766)
LexToken(STRING,'" "',39,769)
LexToken(CONCAT,'.',39,773)
LexToken(VARIABLE,'$mensaje',39,775)
LexToken(SEMICOLON,';',39,783)
LexToken(VARIABLE,'$vacio',40,785)
LexToken(COALESCEEQUAL,'??=',40,792)
LexToken(STRING,"'defecto'",40,796)
LexToken(SEMICOLON,';',40,805)
LexToken(IF,'if',43,835)
LexToken(LPAREN,'(',43,838)
LexToken(VARIABLE,'$entero',43,839)
LexToken(IDENTICAL,'===',43,847)
LexToken(INTEGER,42,43,851)
LexToken(LAND,'&&',43,854)
LexToken(VARIABLE,'$real',43,857)
LexToken(NOTEQUAL,'!=',43,863)
LexToken(INTEGER,0,43,866)
LexToken(LOR,'||',43,868)
LexToken(NOT,'!',43,871)
LexToken(VARIABLE,'$activo',43,872)
LexToken(RPAREN,')',43,879)
LexToken(LBRACE,'{',43,881)
LexToken(ECHO,'echo',44,887)
LexToken(STRING,'"Iguales"',44,892)
LexToken(SEMICOLON,';',44,901)
LexToken(RBRACE,'}',45,903)
LexToken(ELSEIF,'elseif',45,905)
LexToken(LPAREN,'(',45,912)
LexToken(VARIABLE,'$entero',45,913)
LexToken(SPACESHIP,'<=>',45,921)
LexToken(VARIABLE,'$real',45,925)
LexToken(RPAREN,')',45,930)
LexToken(LBRACE,'{',45,932)
LexToken(PRINT,'print',46,938)
LexToken(LPAREN,'(',46,943)
LexToken(STRING,'"Distintos"',46,944)
LexToken(RPAREN,')',46,955)
LexToken(SEMICOLON,';',46,956)
LexToken(RBRACE,'}',47,958)
LexToken(ELSE,'else',47,960)
LexToken(LBRACE,'{',47,965)
LexToken(VARIABLE,'$resultado',48,971)
LexToken(EQUAL,'=',48,982)
LexToken(VARIABLE,'$entero',48,984)
LexToken(GREATEREQUAL,'>=',48,992)
LexToken(INTEGER,10,48,995)
LexToken(QUESTION,'?',48,998)
LexToken(STRING,"'grande'",48,1000)
LexToken(COLON,':',48,1009)
LexToken(STRING,"'pequeno'",48,1011)
LexToken(SEMICOLON,';',48,1020)
LexToken(RBRACE,'}',49,1022)
LexToken(FOR,'for',52,1035)
LexToken(LPAREN,'(',52,1039)
LexToken(VARIABLE,'$i',52,1040)
LexToken(EQUAL,'=',52,1043)
LexToken(INTEGER,0,52,1045)
LexToken(SEMICOLON,';',52,1046)
LexToken(VARIABLE,'$i',52,1048)
LexToken(LESS,'<',52,1051)
LexToken(INTEGER,10,52,1053)
LexToken(SEMICOLON,';',52,1055)
LexToken(VARIABLE,'$i',52,1057)
LexToken(INCREMENT,'++',52,1059)
LexToken(RPAREN,')',52,1061)
LexToken(LBRACE,'{',52,1063)
LexToken(IF,'if',53,1069)
LexToken(LPAREN,'(',53,1072)
LexToken(VARIABLE,'$i',53,1073)
LexToken(ISEQUAL,'==',53,1076)
LexToken(INTEGER,5,53,1079)
LexToken(RPAREN,')',53,1080)
LexToken(CONTINUE,'continue',53,1082)
LexToken(SEMICOLON,';',53,1090)
LexToken(IF,'if',54,1096)
LexToken(LPAREN,'(',54,1099)
LexToken(VARIABLE,'$i',54,1100)
LexToken(LESSEQUAL,'<=',54,1103)
LexToken(INTEGER,8,54,1106)
LexToken(RPAREN,')',54,1107)
LexToken(BREAK,'break',54,1109)
LexToken(SEMICOLON,';',54,1114)
LexToken(RBRACE,'}',55,1116)
LexToken(VARIABLE,'$lista',57,1119)
LexToken(EQUAL,'=',57,1126)
LexToken(LBRACKET,'[',57,1128)
LexToken(INTEGER,1,57,1129)
LexToken(COMMA,',',57,1130)
LexToken(INTEGER,2,57,1132)
LexToken(COMMA,',',57,1133)
LexToken(INTEGER,3,57,1135)
LexToken(RBRACKET,']',57,1136)
LexToken(SEMICOLON,';',57,1137)
LexToken(FOREACH,'foreach',58,1139)
LexToken(LPAREN,'(',58,1147)
LexToken(VARIABLE,'$lista',58,1148)
LexToken(AS,'as',58,1155)
LexToken(VARIABLE,'$clave',58,1158)
LexToken(DOUBLE_ARROW,'=>',58,1165)
LexToken(VARIABLE,'$valor',58,1168)
LexToken(RPAREN,')',58,1174)
LexToken(LBRACE,'{',58,1176)
LexToken(VARIABLE,'$total',59,1182)
LexToken(EQUAL,'=',59,1189)
LexToken(VARIABLE,'$valor',59,1191)
LexToken(COALESCE,'??',59,1198)
LexToken(INTEGER,0,59,1201)
LexToken(SEMICOLON,';',59,1202)
LexToken(RBRACE,'}',60,1204)
LexToken(WHILE,'while',62,1207)
LexToken(LPAREN,'(',62,1213)
LexToken(VARIABLE,'$entero',62,1214)
LexToken(GREATER,'>',62,1222)
LexToken(INTEGER,0,62,1224)
LexToken(RPAREN,')',62,1225)
LexToken(LBRACE,'{',62,1227)
LexToken(VARIABLE,'$entero',63,1233)
LexToken(DECREMENT,'--',63,1240)
LexToken(SEMICOLON,';',63,1242)
LexToken(RBRACE,'}',64,1244)
LexToken(FUNCTION,'function',67,1274)
LexToken(ID,'sumar',67,1283)
LexToken(LPAREN,'(',67,1288)
LexToken(ID,'int',67,1289)
LexToken(ELLIPSIS,'...',67,1293)
LexToken(VARIABLE,'$numeros',67,1296)
LexToken(RPAREN,')',67,1304)
LexToken(COLON,':',67,1305)
LexToken(ID,'int',67,1307)
LexToken(LBRACE,'{',68,1311)
LexToken(RETURN,'return',69,1317)
LexToken(ID,'array_sum',69,1324)
LexToken(LPAREN,'(',69,1333)
LexToken(VARIABLE,'$numeros',69,1334)
LexToken(RPAREN,')',69,1342)
LexToken(SEMICOLON,';',69,1343)
LexToken(RBRACE,'}',70,1345)
LexToken(TRY,'try',72,1348)
LexToken(LBRACE,'{',72,1352)
LexToken(VARIABLE,'$obj',73,1358)
LexToken(EQUAL,'=',73,1363)
LexToken(NEW,'new',73,1365)
LexToken(ID,'Cuadrado',73,1369)
LexToken(LPAREN,'(',73,1377)
LexToken(INTEGER,4,73,1378)
LexToken(RPAREN,')',73,1379)
LexToken(SEMICOLON,';',73,1380)
LexToken(VARIABLE,'$area',74,1386)
LexToken(EQUAL,'=',74,1392)
LexToken(VARIABLE,'$obj',74,1394)
LexToken(NULLSAFE_ARROW,'?->',74,1398)
LexToken(ID,'area',74,1401)
LexToken(LPAREN,'(',74,1405)
LexToken(RPAREN,')',74,1406)
LexToken(SEMICOLON,';',74,1407)
LexToken(RBRACE,'}',75,1409)
LexToken(CATCH,'catch',75,1411)
LexToken(LPAREN,'(',75,1417)
LexToken(ID,'Exception',75,1418)
LexToken(VARIABLE,'$e',75,1428)
LexToken(RPAREN,')',75,1430)
LexToken(LBRACE,'{',75,1432)
LexToken(THROW,'throw',76,1438)
LexToken(VARIABLE,'$e',76,1444)
LexToken(SEMICOLON,';',76,1446)
LexToken(RBRACE,'}',77,1448)
LexToken(FINALLY,'finally',77,1450)
LexToken(LBRACE,'{',77,1458)
LexToken(UNSET,'unset',78,1464)
LexToken(LPAREN,'(',78,1469)
LexToken(VARIABLE,'$obj',78,1470)
LexToken(RPAREN,')',78,1474)
LexToken(SEMICOLON,';',78,1475)
LexToken(RBRACE,'}',79,1477)
LexToken(VARIABLE,'$doble',81,1480)
LexToken(EQUAL,'=',81,1487)
LexToken(FN,'fn',81,1489)
LexToken(LPAREN,'(',81,1491)
LexToken(VARIABLE,'$x',81,1492)
LexToken(RPAREN,')',81,1494)
LexToken(DOUBLE_ARROW,'=>',81,1496)
LexToken(VARIABLE,'$x',81,1499)
LexToken(TIMES,'*',81,1502)
LexToken(INTEGER,2,81,1504)
LexToken(SEMICOLON,';',81,1505)
Lexical error: variable invalida '$1malo' en linea 84
LexToken(EQUAL,'=',84,1534)
LexToken(INTEGER,5,84,1536)
LexToken(SEMICOLON,';',84,1537)
LexToken(VARIABLE,'$x',85,1539)
LexToken(EQUAL,'=',85,1542)
Lexical error: identificador invalido '9abc' en linea 85
LexToken(SEMICOLON,';',85,1548)
LexToken(VARIABLE,'$y',86,1550)
LexToken(EQUAL,'=',86,1553)
LexToken(INTEGER,7,86,1555)
Lexical error: '`' en linea 86
LexToken(INTEGER,2,86,1559)
LexToken(SEMICOLON,';',86,1560)
LexToken(CLOSE_TAG,'?>',87,1562)
```
