<?php
	
	if ($_POST){
		$resul = 0;
		$primer = $_POST['primer'];
		$segundo = $_POST['segundo'];

		if (intval($_POST['operacion']) == 1){
			$resul = $primer + $segundo;
		}else if (intval($_POST['operacion']) == 2){
			$resul = $primer - $segundo;
		}else if (intval($_POST['operacion']) == 3){
			$resul = $primer * $segundo;
		}else if (intval($_POST['operacion']) == 4){
			if ($segundo > 0)
				$resul = $primer / $segundo;
			else
				$resul = 'Operacion Invalida';
		}else if (intval($_POST['operacion']) == 5){	
			if ($segundo > 0)
				$resul = $primer % $segundo;
			else
				$resul = 'Operacion Invalida';
		}	
		header("Location: calculadora.php?primer=$primer&segundo=$segundo&resultado=$resul");
	}
	else
	{
		echo 'Error en la llamada de POST';
	}


?>