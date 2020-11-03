<html>
	<head>
		<title>
			Pagina de recepcion de variables
		</title>
	</head>

	<body>

		<h1> Se obtuvieron las siguientes variables: </h1>

		<?php

			$b = $_GET['b'];
			$c = $_GET['c'];

			echo "Var b = ". $b."<br>";
			echo "Var c = ". $c."<br>";

		?>
	</body>
</html>