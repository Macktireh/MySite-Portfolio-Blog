const form = document.querySelector("form");
const inputs = document.querySelectorAll(
  'input[type="text"], input[type="email"], textarea'
);
// const progressBar = document.getElementById("progress-bar");
let name, email, message;

const errorDisplay = (tag, message_error, valid) => {
  const container = document.querySelector("." + tag + "-container");
  const span = document.querySelector("." + tag + "-container > span");

  if (!valid) {
    container.classList.add("error");
    span.textContent = message_error;
  } else {
    container.classList.remove("error");
    span.textContent = message_error;
  }
};

const nameChecker = (value) => {
  if (value.length > 0 && (value.length < 3 || value.length > 30)) {
    errorDisplay("name", "Le nom doit faire entre 3 et 30 caractères");
    name = null;
  } else if (!value.match(/^[a-zA-Z -]*$/)) {
    errorDisplay(
      "name",
      "Le nom ne doit pas contenir de numéro et caractères spéciaux"
    );
    name = null;
  } else {
    errorDisplay("name", "", true);
    name = value;
  }
};

const emailChecker = (value) => {
  if (!value.match(/^[\w_-]+@[\w-]+\.[a-z]{2,4}$/i)) {
    errorDisplay("email", "Le mail n'est pas valide");
    email = null;
  } else {
    errorDisplay("email", "", true);
    email = value;
  }
};

const messageChecker = (value) => {
  if (value.length > 0 && (value.length < 10 || value.length > 5000)) {
    errorDisplay(
      "message",
      "Le message doit contenir entre 10 et 5000 caractères"
    );
    message = null;
  } else {
    errorDisplay("message", "", true);
    message = value;
  }
};

inputs.forEach((input) => {
  input.addEventListener("input", (e) => {
    switch (e.target.name) {
      case "name":
        nameChecker(e.target.value);
        break;
      case "email":
        emailChecker(e.target.value);
        break;
      case "message":
        messageChecker(e.target.value);
        break;
      default:
        nul;
    }
  });
});

// form.addEventListener("submit", (e) => {
//   // e.preventDefault();

//   if (name && email && message) {
//     // const data = {
//     //   name,
//     //   email,
//     //   message,
//     // };
//     // console.log(data);
//     // inputs.forEach((input) => (input.value = ""));
//     // progressBar.classList = "";
//     // name = null;
//     // email = null;
//     // message = null;
//     // alert("Inscription validée !");
//   } else {
//     e.preventDefault();
//     alert("veuillez remplir correctement les champs");
//   }
// });
