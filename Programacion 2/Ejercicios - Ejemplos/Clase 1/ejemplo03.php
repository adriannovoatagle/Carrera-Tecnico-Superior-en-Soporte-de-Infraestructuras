<html>
	<head>
		<title>Página de envío</title> 
	</head>
	<body>
		<h1>Envío de variables a otra página.</h1>
		<?php  
			$a = "Hola, ";
			$b = "bienvenido a mi página";
			echo "Enviar las siguientes variables:<br/>";
			echo "a = $a <br/>";
			echo "b = $b <br/>";
		?>
		<p>Pulsar el siguiente enlace</p>
		<?php  
			echo "<a href='ejemplo04.php?a=$a&b=$b'>Enviar variables</a>";
		?>
	</body>
</html>