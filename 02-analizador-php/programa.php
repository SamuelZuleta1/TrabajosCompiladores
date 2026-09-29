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
