<?php

	$num = 15;
	$cadena = 'Esto es un string';
	$decimal = 10.5;
	$animales = array("perro", "gato", "pajaro", "caballo");
	
	echo $num;
	echo '<br/>';
	
	echo $cadena;
	echo '<br/>';
	
	echo $decimal;
	echo '<br/>';
	
	var_dump($animales);
	echo '<br/>';
	
	print_r($animales);
	echo '<br/>';

	var_dump($animales[1]);
	echo '<br/>';

	echo $animales[1];
	echo '<br/>';

	var_dump ($num, $decimal, $cadena);
?>