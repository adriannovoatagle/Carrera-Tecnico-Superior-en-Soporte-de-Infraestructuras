<?php

/* 
	Agregue el nombre del color
*/

?>

<html>
<head>
	<title>Clase 2 Ejemplo 6</title>
</head>
<body>

	<h1>Seleccion de color</h1>

	<?php

		$color = "verde";
		echo "Color seleccionado: ".$color."<br>"."<br>";

		switch($color){
			case "verde":
				echo "Color Verde";
				break;
			case "amarillo":
				echo "Color Amarillo";
				break;
			case "azul":
				echo "Color Azul";
				break;
			default:
				echo "El color elegido no se encuentra. Colores válidos: verde, amarillo, azul";	
				break;
		}
	?>

</body>
</html>