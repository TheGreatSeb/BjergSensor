let colorImage = document.getElementById("colorImage");
let button2 = document.getElementById("button2");

function changeToBW() {

    if (colorImage.getAttribute('src') === "./img1.png") {
        colorImage.setAttribute('src', "./img2.jpg");
    }
    else {
        colorImage.setAttribute('src', "./img1.png");
    }
}

button2.addEventListener("click", changeToBW);