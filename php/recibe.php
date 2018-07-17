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


?>

