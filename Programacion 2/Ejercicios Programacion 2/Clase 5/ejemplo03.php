<?php

	//Funciones Matematicas
	//ABS 
	$num = -10;
	var_dump(abs($num));
	echo "<br> <br>";

	//EXP
	$num = 10;
	var_dump(exp($num));
	echo "<br> <br>";

	//HEXDEC
	var_dump(hexdec(10));
	echo "<br> <br>";

	//LOG10
	var_dump(log10($num));
	echo "<br> <br>";

	//LOG
	var_dump(log($num));
	echo "<br> <br>";

	//MAX
	var_dump(max(2, 4, 6, 48, 30));
	echo "<br> <br>";

	//MIN
	var_dump(min(2, 4, 6, 8, 10));
	echo "<br> <br>";
	
	//MT_RAND
	var_dump(mt_rand(1, 1000000));
	echo "<br> <br>";
	
	//SQRT
	$num = 9;
	var_dump(sqrt($num));
	echo "<br> <br>";
?>