// ===============================
// DOM Elements
// ===============================

const passwordInput = document.getElementById("password");
const togglePassword = document.getElementById("togglePassword");
const eyeIcon = document.getElementById("eyeIcon");

const usernameInput = document.querySelector("input[name='username']");
const loginForm = document.querySelector("form");
const loginButton = document.querySelector(".login-btn");


// ===============================
// Auto Focus
// ===============================

window.addEventListener("load", () => {

    if (usernameInput) {
        usernameInput.focus();
    }

});


// ===============================
// Show / Hide Password
// ===============================

togglePassword.addEventListener("click", () => {

    if (passwordInput.type === "password") {

        passwordInput.type = "text";

        eyeIcon.classList.remove("fa-eye");
        eyeIcon.classList.add("fa-eye-slash");

    } else {

        passwordInput.type = "password";

        eyeIcon.classList.remove("fa-eye-slash");
        eyeIcon.classList.add("fa-eye");

    }

});


// ===============================
// Login Button Animation
// ===============================

loginForm.addEventListener("submit", () => {

    loginButton.disabled = true;

    loginButton.innerHTML = `
        <i class="fa-solid fa-spinner fa-spin"></i>
        Logging In...
    `;

});


// ===============================
// Enter Key Support
// ===============================

document.addEventListener("keydown", function(event){

    if(event.key === "Enter"){

        loginForm.requestSubmit();

    }

});