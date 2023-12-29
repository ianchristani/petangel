let theUrl = window.location.pathname;
let locatorContent = document.getElementById("finder");


switch (theUrl) {
    case "/login/":
      locatorContent.innerHTML = "zaloguj się";
    break;
    case "/signup/":
      locatorContent.innerHTML = "zarejestruj się";
    break;
    default:
        locatorContent.innerHTML = "strona główna";
  }