<?php

//print_r($_POST);

// si usamos el método get enviaremos los valores por url
if (!$_POST) {
  // Estamos redirigiendo, lo ideal sería hacerlo hacia nuestro formulario
  header('Location: http://www.google.com')
}

$user = $_POST['user'];
$mail = $_POST['mail'];
$password = $_POST['password'];
$password_2 = $_POST['password_2'];
$age = $_POST['age'];

// denemos abrir coneción con la base de datos, comprobar si la clave primaria que será el mail
// ya está registrada y si no añadir los campos. En ambos casos mostrar un mensaje al usuario.

// link with the data bases
$link = mysql_connect('mysql_host', 'mysql_user', 'mysql_password') or die('no se puede conectar: ' . mysql_error());
echo 'Connected successfully';
mysql_select_db('my_database') or die('No se pudo seleccionar la base de datos');

// realizar la consulta de la base de datos, AQUÍ DEBEREMOS HACER LA COMPROBACIÓN POR LA CLAVE PRIMARIA
$query = 'SELECT * FROM my_table';
$result = mysql_query($query) or die('Consulta fallida: ' .mysql_error());

$ya_en_base = FALSE; // El usuario no está registrado ya
// AQUÍ DEBERÁN ESRTAR LAS CONDICIONES SOBRE LA BASE DE DATOS, AÑADIREMOS LOS RESULTADOS SI ES NECESIAO

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

// cerrar la conexión
mysql_close($link);
?>
