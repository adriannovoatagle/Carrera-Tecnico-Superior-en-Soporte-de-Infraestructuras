<html>
	<meta charset="utf8"/>
	<head> 
		<title>Calculadora</title>
	</head>
	<body>
		<h1>Calculadora</h1>
		<form method="post" action="operacion.php">
			<label>Primer N&uacute;mero:</label>
			<input type="number" name="primer" value="<?php echo $_GET['primer']; ?>">
			<br>
			<br>
			<label>Segundo N&uacute;mero:</label>
			<input type="number" name="segundo" value="<?php echo $_GET['segundo']; ?>">
			<h5>Tipo de Operaci&oacute;n </h5>
			<input type="radio" name="operacion" value="1" checked="true"> Suma <br>
			<input type="radio" name="operacion" value="2"> Resta <br>
			<input type="radio" name="operacion" value="3"> Multiplicaci&oacute;n <br>
			<input type="radio" name="operacion" value="4"> Divisi&oacute;n <br>
			<input type="radio" name="operacion" value="5"> Divisi&oacute;n con Resto
			<br>
			<br>
			<input type="submit" name="enviar" value="Enviar">			
		</form>
		<br>
		<br>
		<label>Resultado:</label>
		<input type="text" name="resultado" value="<?php if (isset($_GET['resultado']))  echo $_GET['resultado'];  ?>">
	</body>
	<br><br><br><br><br><br>
	<br><br><br><br><br><br>
<footer>
	Calculadora
</footer>