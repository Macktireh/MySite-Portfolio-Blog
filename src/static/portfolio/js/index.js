/* =================== Responsive navbar =================== */

const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const navLink = document.querySelector(".nav-link");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
  navLink.classList.toggle("active");
});

/* =================== Button pour remonter en haut de la page =================== */

const BtnTop = document.querySelector(".btn-top");
const arrow_up = document.getElementById("arrow-up");

window.addEventListener("scroll", () => {
  if (window.scrollY > 650) {
    BtnTop.classList.add("btn-top-show");
  } else BtnTop.classList.remove("btn-top-show");
});

BtnTop.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
  arrow_up.classList.add("arrow-up-click");
});

// arrow_up.addEventListener("click", () => {
//   arrow_up.classList.add("arrow-up-click");
// });
