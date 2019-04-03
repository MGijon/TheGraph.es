const introduction_text_english = "hello world"
// Inicialmente estará en inglés, decalro como constantes todos los textos y me los guardo, luego creo las traducciones y las 
// escribo como constantes aquí, el botón hará el cambio entre ambos -> solo necesitaré una función para cambiar de idioma!!

function changetoSpanish() {
    document.getElementById("spanish-button").onclick = function () {
        texto_introduction = document.getElementById("introduction-text");
        texto_introduction.innerHTML = introduction_text_english;
    };
}

function changetoEnglish() {
    document.getElementById("english-button").style.color = "green";
}

changetoEnglish()
changetoSpanish()

// https://www.w3schools.com/js/js_whereto.asp
// https://www.w3schools.com/jsref/event_onclick.asp
