var password;
var correcta = '12345';
password = prompt('Enter password to access', '');
if (password == correcta){
  alert('Correct!! Enjoy the graph');
}
else{
  window.location="http://thegraph.es"
}
