<?php

	function recursividad($a, $bandera)
	{		
	    if ($a < 20) {
	        echo "$a \n";
	        recursividad($a + 1, true);	        
	    }else{
	    	if ($bandera == false)
	    		echo 'No se cumple las condiciones';	    	
	    }
	}

	recursividad(1, false);
?>