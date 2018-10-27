<?php

if (!$_POST) {
  // redireccionamos si no llegan los datos
  header('Location: https://www.google.com')
}

$user = $_POST['user']; // debo buscar si existe en la base de datos y si existe pasare a comprobar la contraseña
$pass = $_POST['password'];

// link with the data bases
$link = mysql_connect('mysql_host', 'mysql_user', 'mysql_password') or die('no se puede conectar: ' . mysql_error());
echo 'Connected successfully';
mysql_select_db('my_database') or die('No se pudo seleccionar la base de datos');
/*
// realizar la consulta de la base de datos
$query = 'SELECT * FROM my_table';
$result = mysql_query($query) or die('Consulta fallida: ' .mysql_error());

// imprimir los resultados en html
echo "<table>\n"
while ($line = mysql_fetch_array($result, MYSQL_ASSOC)) {
  echo "\t<tr>\n";
  foreach ($line as $col_value) {
    echo "\t\t<td>$col_value</td>\n";
  }
  echo "\t</tr>\n";
}
echo "</table>\n";

// liberar resultados
mysql_free_result($result);
*/
// cerrar la conexión
mysql_close($link);
 ?>
