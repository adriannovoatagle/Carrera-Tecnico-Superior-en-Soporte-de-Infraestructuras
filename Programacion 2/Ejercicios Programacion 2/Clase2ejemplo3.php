<?php

/*
	Se debe solicitar un numero para el calculo del año
	El año no puede ser un número decimal.
	El año debe ser positivo e inferior a 10.000.
	El año puede ser cero.
	Los años bisiestos son múltiplos de 4
*/

?>

<html>
<head>
	<title>Clase 2 Ejemplo 3</title>
</head>
<body>
	<h1>Año bisiesto</h1>
	<?php

		$num = 2020;

		echo "Año = ".$num."<br>"."<br>";

		if($num >= 0 && $num < 10000 && is_int($num)){
			if($num % 4 == 0){
				echo "El año es bisiesto";
			}else{
				echo "El año no es bisiesto";
			}
		}else{
			echo "El numero no cumple con los parametros establecidos";
		}
	?>
</body>
</html>