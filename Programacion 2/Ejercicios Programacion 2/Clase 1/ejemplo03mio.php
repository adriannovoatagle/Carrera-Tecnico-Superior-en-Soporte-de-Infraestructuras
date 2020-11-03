<html>
	<head>
		<title>
			Pagina de envio
		</title>
	</head>
	<body>
		<h1>
			Se enviaran las siguientes variables
		</h1>
		<?php

			$b = 4;
			$c = 5;

			echo "Var b = ". $b . "<br>";
			echo "Var c = ". $c . "<br>";
		?>
		<p>Pulsar el siguiente enlace:</p>
		<?php
			echo "<a href='ejemplo04mio.php?b=$b&c=$c'>Enviar variables</a>";
		?>		
		
	</body>
</html>