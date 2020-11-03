<?php

/* 
	Agregue una nota para indicar la calificacion
	La nota debe ser mayor a cero y maximo 10
	No se permiten notas mayores a 10
*/

?>

<html>
<head>
	<title>Clase 2 Ejemplo 5</title>
</head>
<body>

	<h1>Nota </h1>

	<?php

		$nota = 10;
		
		echo "Valor de nota: ".$nota."<br>"."<br>";

		switch ($nota) {
			case ($nota > 0 && $nota < 4):
				echo "Desaprobado";
				break;
			case ($nota >=4 && $nota < 11):
				echo "Aprobado";
				break;
			default:
				echo "La nota se encuentra fuera del rango permitido (1 al 10)";
				break;
		}

	?>

</body>
</html>