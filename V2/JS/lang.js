const introduction_text= "hello world"
// Inicialmente estará en inglés, decalro como constantes todos los textos y me los guardo, luego creo las traducciones y las 
// escribo como constantes aquí, el botón hará el cambio entre ambos -> solo necesitaré una función para cambiar de idioma!!

// Necesito saber como cargar las traduccinoes de algún archivo externo

function language() {
    texto_introduction = document.getElementById("introduction-text");
    
    document.getElementById("spanish-button").onclick = function () {    
        texto_introduction.innerHTML = introduction_text;
    };
    
    document.getElementById("english-button").onclick = function() {
        texto_introduction.innerHTML = "alright motherfucker!!"  
    };
}


language()

// https://www.w3schools.com/js/js_whereto.asp
// https://www.w3schools.com/jsref/event_onclick.asp
// https://www.w3schools.com/js/js_hoisting.asp
// https://www.w3schools.com/jsref/event_onclick.asp