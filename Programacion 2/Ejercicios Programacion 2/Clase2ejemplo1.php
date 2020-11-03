<?php
/*
	Ingresar el dividendo y el divisor.
	El dividendo y el divisor pueden ser números decimales.
	El dividendo y el divisor deben ser positivos e inferiores a 1.000.
	El divisor tiene que ser un número diferente de cero, pero el dividendo puede ser cero.
	Mostra el cociente y el resto de la division
*/
?>
<html>
<head>
	<title>Clase 2 Ejemplo 1</title>
</head>
<body>
	<h1> Division </h1>
	<?php

		$dividendo = 10;
		$divisor = 2;
		echo "Dividendo = ".$dividendo."<br>";
		echo "Divisor = ".$divisor."<br>";

		if(($dividendo >= 0 && $dividendo < 1000.0) && ($divisor > 0 && $divisor < 1000.0)){
			echo "Cociente = ". ($dividendo/$divisor)."<br>";
			echo "Resto = ". ($dividendo%$divisor);
		}else{
			echo "Los numeros no cumplen con los parametros establecidos";
		}

	?>

</body>
</html>
