<?php

if (!$_POST) {
  // redireccionamos si no llegan los datos
  header('Location: https://www.google.com')
}

$user = $_POST['user']; // debo buscar si existe en la base de datos y si existe pasare a comprobar la contraseña
$pass = $_POST['password'];


 ?>
