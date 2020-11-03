<html>
	<head>
		<title>Página de destino</title> 
	</head>
	<body>
		<h1>Al abrir esta página se han pasado las siguientes variables:</h1>
		<?php  
			$a = $_GET['a'];
			$b = $_GET['b'];
			echo "<p>variable a : $a";
			echo "<p>variable b : $b";
		?>
	</body>
</html>