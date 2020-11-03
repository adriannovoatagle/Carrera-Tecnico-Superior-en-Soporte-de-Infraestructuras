<html>
<head>
	<title>Ejercicios Funciones</title>
</head>
<body>
	<?php
		$e1 = 2;
		$e2 = 1;
		$e41 = 10;
		$e42 = 2;
		$e5b = 5;
		$e5h = 5;
		$e6precio = 20;
		$e7 = 5;
		$e8 = 11;
		$e91 = 10;
		$e92 = 12;
		$e101 = 2;
		$e102 = 3;
		$e103 = 1;
		$e11 = "hola";
		$e12 = "a";
		$e13 = [1,2,3,4];
		$e14 = "hola";
		$e15 = "radar";
		$e161 = [1,2,3,4];
		$e162 = [2,5,6,7];
		$e171 = 5;
		$e172 = "a";
		$e18 = [1,2,3];
		$e19 = [1,2,3,4];
		$e20 = [1,2,3,4];

		function ejercicio1($x){
			if($x % 2 == 0){
				echo "Ejercicio 1. El numero $x es par.<br>";
			}else{
				echo "Ejercicio 1. El numero $x es impar.<br>";
			}
		}

		function ejercicio2($x){
			if($x % 2 == 0){
				return "Ejercicio 2. El numero $x es par.<br>";
			}else{
				return "Ejercicio 2. El numero $x es impar.<br>";
			}
		}

		function ejercicio4($x,$y){
			return "Ejercicio 4. El resto de la division entre $x y $y es: ".$x % $y.".<br>";
		}

		function ejercicio5($x,$y){
			$r = ($x * $y) / 2;
			echo "Ejercicio 5. El area del triangulo es: $r.<br>";
		}

		function ejercicio6($x){
			$r = $x * 1.21;
			echo "Ejercicio 6. El precio del producto es: $x. El precio con IVA incluido es: $r.<br>";
		}

		function ejercicio7($x){

			$r = 1;
			for($i = 1; $i <= $x;$i++){
				$r *= $i;
			}
			
			return "Ejercicio 7. El factorial del numero $x es: $r.<br>";
		}

		function ejercicio8($x){

			$cr = 0;

			for($i = 1; $i <= $x;$i++){
				if($x % $i == 0){
					$cr += 1;
				}
			}
			
			if($cr == 2){
				echo "Ejercicio 8. El numero $x es primo.<br>";
			}else{
				echo "Ejercicio 8. El numero $x no es primo.<br>";	
			}
		}

		function ejercicio9($x,$y){
			
			if($x > $y){
				return "Ejercicio 9. $x es mayor que $y.<br>";
			}else{
				return "Ejercicio 9. $y es mayor que $x.<br>";
			}
			
		}

		function ejercicio10($x,$y,$z){
			
			if($x > $y && $x > $z){
				return "Ejercicio 10. Num1: $x. Num2: $y. Num3: $z. $x es el mayor.<br>";
			}elseif($y > $x && $y > $z){
				return "Ejercicio 10. Num1: $x. Num2: $y. Num3: $z. $y es el mayor.<br>";
			}else{
				return "Ejercicio 10. Num1: $x. Num2: $y. Num3: $z. $z es el mayor.<br>";
			}
			
		}

		function ejercicio11($x){
	
			if(gettype($x) == "string"){
				$r = strlen($x);
				echo "Ejercicio 11. Longitud = $r.<br>";
			}
			if(gettype($x) == "array"){
				$r = count($x);
				echo "Ejercicio 11. Longitud = $r.<br>";
			}
			
		}

		function ejercicio12($x){
	
			$v = ["a","e","i","o","u"];

			foreach ($v as $key) {
				if($key == $x){
					return "Ejercicio 12. ".True." (True).<br>";
				}else{
					return "Ejercicio 12. ".False." 0 (False).<br>";
				}
			}
		}

		function ejercicio13($x){
			
			$rs = 0;
			$rm = 1;

			foreach($x as $key){
				$rs += $key;
				$rm *= $key;
			}
			return "Ejercicio 13. Suma de la lista = $rs. Multiplicacion de la lista = $rm.<br>";	
		}

		function ejercicio14($x){

			$r = "";
			for($i = 1; $i <= strlen($x);$i++){
				$r = $r.$x[-$i];
				
			}
			return "Ejercicio 14. Cadena: $x. Cadena invertida: $r. <br>";
		}

		function ejercicio15($x){

			$r = "";
			for($i = 1; $i <= strlen($x);$i++){
				$r = $r.$x[-$i];
				
			}
			if($r == $x){
				return "Ejercicio 15. ".True." (True).<br>";
			}else{
				return "Ejercicio 15. ".False." 0 (False).<br>";
			}
		}

		function ejercicio16($x,$y){

			$r = 0;
			foreach ($x as $kx => $vx) {
				foreach ($y as $ky => $vy) {
			 		if($vy == $vx){
						$r += 1;
					}else{
						$r += 0;
					}
				}
			}
			
			if($r == 1){
				return "Ejercicio 16. ".True." (True).<br>";
			}else{
				return "Ejercicio 16. ".False." 0 (False).<br>";
			}
			
		}

		function ejercicio17($x,$y){

			$r = "";
			for($i = 0;$i < $x;$i++){
				$r = $r.$y;
			}
			return "Ejercicio 17. Numero: $x. Letra: $y. Resultado: $r.";
		}

		function ejercicio18($x){

			$r = 0;
			$rl = array();

			for($i = 0;$i < count($x);$i++){
				$r += $x[$i];
				$rl[$i] = $r;
			}
			echo "<br>Ejercicio 18. Array original: ";
			print_r($x);
			echo ".Array resultante: ";
			print_r($rl);
			echo "<br>";
		}

		function ejercicio19($x){

			$r = array();
			echo "Ejercicio 19. Array original: ";
			print_r($x);

			unset($x[0]); //borra el primer elemento de un array
			array_pop($x); //borra el ultimo elemento de un array
			
			$r = $x;
			echo ".Array resultante: ";
			print_r($r);
			echo "<br>";
		}

		function ejercicio20($x){

			$r = $x;
			echo "Ejercicio 20. Array original: ";
			print_r($r);

			sort($x);

			echo ".Array resultante: ";
			print_r($x);
						
			if($r == $x){
				echo ". El Array esta ordenado";
			}else{
				echo ". El Array No esta ordenado";
			}
			echo "<br>";

		}

		ejercicio1($e1);
		echo ejercicio2($e2);
		echo "Ejercicio 3 = Ejercicio 9.<br>";
		echo ejercicio4($e41,$e42);
		ejercicio5($e5b,$e5h);
		ejercicio6($e6precio);
		echo ejercicio7($e7);
		ejercicio8($e8);
		echo ejercicio9($e91,$e92);
		echo ejercicio10($e101,$e102,$e103);
		ejercicio11($e11);
		echo ejercicio12($e12);
		echo ejercicio13($e13);
		echo ejercicio14($e14);
		echo ejercicio15($e15);
		echo ejercicio16($e161,$e162);
		echo ejercicio17 ($e171,$e172);
		ejercicio18($e18);
		ejercicio19($e19);
		ejercicio20($e20);
	?>

</body>
</html>
