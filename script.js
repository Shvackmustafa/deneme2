const searchForm = document.querySelector(".search-form");
const cartItem = document.querySelector(".cart-items-container");
const navbar = document.querySelector(".navbar");
//login form
document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");
  const registerForm = document.getElementById("register-form");
  const switchToRegister = document.getElementById("switch-to-register");
  const switchToLogin = document.getElementById("switch-to-login");

  switchToRegister.addEventListener("click", () => {
    loginForm.classList.add("hidden");
    registerForm.classList.remove("hidden");
  });

  switchToLogin.addEventListener("click", () => {
    registerForm.classList.add("hidden");
    loginForm.classList.remove("hidden");
  });
});

function handleLogin() {
  alert("Giriş yapıldı!");
  window.location.href = "homepage.html"; // Ana sayfa yönlendirme
}

function handleRegister() {
  alert("Kayıt başarılı!");
  window.location.href = "homepage.html"; // Ana sayfa yönlendirme
}
// burda login


signupBtn.addEventListener("click", (e) => {
  e.preventDefault();
  formContainer.classList.add("active");

});
loginBtn.addEventListener("click", (e) => {
  e.preventDefault();
  formContainer.classList.remove("active");

});


//! buttons
const searchBtn = document.querySelector("#search-btn");
const cartBtn = document.querySelector("#cart-btn");
const menuBtn = document.querySelector("#menu-btn");


searchBtn.addEventListener("click", function () {
  searchForm.classList.toggle("active");
  document.addEventListener("click", function (e) {
    if (
      !e.composedPath().includes(searchBtn) &&
      !e.composedPath().includes(searchForm)
    ) {
      searchForm.classList.remove("active");
    }
  });
});

cartBtn.addEventListener("click", function () {
  cartItem.classList.toggle("active");
  document.addEventListener("click", function (e) {
    if (
      !e.composedPath().includes(cartBtn) &&
      !e.composedPath().includes(cartItem)
    ) {
      cartItem.classList.remove("active");
    }
  });
});
//slider özelliği 
function moveSlider(sliderId, direction) {
  const slider = document.getElementById(sliderId);
  const boxWidth = slider.querySelector('.box').offsetWidth;
  const currentTransform = getComputedStyle(slider).transform.match(/-?\d+(\.\d+)?/g);
  const currentX = currentTransform ? parseFloat(currentTransform[4]) : 0;
  const maxTranslateX = -(slider.children.length - 1) * boxWidth;
  

  let newTranslateX = currentX - direction * boxWidth;

  if (newTranslateX > 0) newTranslateX = 0;
  if (newTranslateX < maxTranslateX) newTranslateX = maxTranslateX;

  slider.style.transform = `translateX(${newTranslateX}px)`;
}// burdada slider bitiyor

menuBtn.addEventListener("click", function () {
  navbar.classList.toggle("active");
  document.addEventListener("click", function (e) {
    if (
      !e.composedPath().includes(menuBtn) &&
      !e.composedPath().includes(navbar)
    ) {
      navbar.classList.remove("active");
    }
  });
});