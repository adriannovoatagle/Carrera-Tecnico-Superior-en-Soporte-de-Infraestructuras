<?php
	//Definir variables a utilizar
	$a = 20;
	$b = 10;
	$c = 3;
	
	//Suma
	$suma = $a + $b;
	
	//Resta
	$resta = $b - $c;
	
	//Multiplicacion
	$mult = $a * $b;
	
	//Division 
	$div = $b / $c;
	
	//Division con resto 
	$resto = $b % $c;
	
	//Incremento de una variables
	$a++;
	
	//Decremento de una variables
	$c--;
	
	//Asignacilon en $b de la suma de $b + $c
	$b += $c;
	
	//Imprimir resultados
	echo "La suma es: " . $suma . " <br/>";
	echo "La resta es: " . $resta . " <br/>";
	echo "La multiplicacion es: " . $mult . " <br/>";
	echo "La division es: " . $div . " <br/>";
	echo "El resto de la division es: " . $resto . " <br/>";
	
	echo "Incremento en a: " . $a . " <br/>";
	echo "Decremento en c: " . $c . " <br/>";
	echo "Asignacion en b: " . $b . " <br/>";	
?>