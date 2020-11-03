<?php

	/*
	Se solicitan tres números.
	Los números pueden ser decimales.
	Los números deben ser superiores a -1.000 e inferiores a 1.000.
	Se debe indicar si los tres números son iguales, si hay dos iguales o si los tres son distintos.
*/
?>
<html>
<head>
	<title>Clase 2 Ejemplo 2</title>
</head>
<body>
	<h1> Comparacion entre 3 numeros</h1>
	<?php

	$num1 = 10;
	$num2 = 10;
	$num3 = 10;

	echo "Numero 1 = ".$num1."<br>";
	echo "Numero 2 = ".$num2."<br>";
	echo "Numero 3 = ".$num3."<br>"."<br>";

	if(($num1 > -1000.0 && $num1 < 1000.0) && ($num2 > -1000.0 && $num2 < 1000.0) && ($num3 > -1000.0 && $num3 < 1000.0)){
		if($num1 == $num2 && $num1 == $num3){
			echo "Los 3 numeros son iguales";
		}elseif($num1 == $num2 && $num1 != $num3){
			echo "Num1 = Num2";	
		}elseif($num1 == $num3 && $num1 != $num2){
			echo "Num1 = Num3";
		}elseif($num2 == $num3 && $num2 != $num1){
			echo "Num2 = Num3";
		}else{
			echo "Los 3 numeros son distintos";
		}
	}

	?>
</body>
</html>