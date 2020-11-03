<?php
	#Comentarios
	//Declaracion de variables
	$a = 5;
	$b = 10;
	$c = 15;
	$d = 20;
	$e = 25;
	
	$suma = 0;
	$resta = 0;
	$mult = 0;
	$div = 0;
	$resto = 0;
	
	//Suma
	$suma = $a + $b + $c + $d + $e;
	echo "El resultado de la suma es: " . $suma . " <br/>";
	
	//Resta
	$resta = $a - $b;
	echo "El resultado de la resta es: " . $resta . " <br/>";
	
	//Multiplicacion
	$mult = $d * $a;
	echo "El resultado de la multiplicacion es: " . $mult . " <br/>";
	
	//Division
	$div = $d / $a;
	echo "El resultado de la division es: " . $div . " <br/>";
	
	//Resto
	$resto = $e % $a;
	echo "El resultado de la division con resto es: " . $resto . " <br/>";
	
	//Operacion
	$a = (((($a + $b) * $e) - $d) / $c) + 1;
	echo "El resultado de la operacion es: " . $a . " <br/>";
	
	echo "El resultado de la operacion anterior redondeado con dos decimales es: " . round($a , 2) . " <br/>";
?>