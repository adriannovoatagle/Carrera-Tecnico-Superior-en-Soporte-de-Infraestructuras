<?php

	//Funciones String
	//EXPLODE 
	$cadena = explode('-', 'prueba-test-hola');
	var_dump($cadena);
	echo "<br> <br>";

	//MD5
	$clave = 'test';
	$enc = md5($clave);
	var_dump($clave, $enc);
	echo "<br> <br>";

	$cadena = ' Esto es una prueba de espacios ';
	var_dump($cadena); 
	echo "<br> <br>";

	//LTRIM
	var_dump('LTRIM', LTRIM($cadena));
	echo "<br> <br>";

	//RTRIM
	var_dump('RTRIM', RTRIM($cadena));
	echo "<br> <br>";

	//TRIM
	var_dump('TRIM', TRIM($cadena));
	echo "<br> <br>";

	//PARSE_STR
	parse_str("nombre=Pedro&edad=43");
	echo "Nombre: " . $nombre . "<br> <br>";
	echo "Edad: " . $edad . "<br> <br>";
	echo "<br> <br>";

	//STR_REPLACE
	echo str_replace("Mundo","Internet","Hola Mundo!");
	echo "<br> <br>";

	//STR_REPEAT
	echo str_repeat("A.",13);
	echo "<br> <br>";

	//STR_SPLIT
	var_dump(str_split("Hola Prueba"));

	echo "<br> <br>";

	//STRIPOS
	echo stripos("Aprendiendo java para el futuro, lenguaje php!","php");
	echo "<br> <br>";

	//STRLEN
	echo strlen("Largo de la cadenaaaaa");
	echo "<br> <br>";

	//STRTOLOWER
	var_dump('PrUeba', strtolower('PrUeba'));
	echo "<br> <br>";


	//STRTOUPPER
	var_dump('PrUeba', strtoupper('PrUeba'));
	echo "<br> <br>";

?>