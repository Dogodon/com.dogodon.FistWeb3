// auth_scripts.js

document.addEventListener("DOMContentLoaded", function () {

    // Ajout d'un effet au bouton de soumission
    const submitButton = document.querySelector(".btn");

    if (submitButton) {
        submitButton.addEventListener("mouseenter", function () {
            submitButton.style.transform = "scale(1.05)";
            submitButton.style.transition = "transform 0.3s";
        });

        submitButton.addEventListener("mouseleave", function () {
            submitButton.style.transform = "scale(1)";
        });
    }

    // Animation de bienvenue pour les utilisateurs
    const container = document.querySelector(".container");
    if (container) {
        container.classList.add("fadeIn");
    }

    // Affichage d'un message d'alerte si un champ est mal rempli
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function (e) {
            let errorMessage = "";
            const usernameField = document.querySelector("input[name='username']");
            const passwordField = document.querySelector("input[name='password']");

            if (!usernameField.value || !passwordField.value) {
                errorMessage = "Veuillez remplir tous les champs!";
            }

            if (errorMessage) {
                e.preventDefault();
                alert(errorMessage);
            }
        });
    }

});
