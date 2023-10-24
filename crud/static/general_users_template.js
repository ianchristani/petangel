let theUrl = window.location.pathname;
let locatorContent = document.getElementById("finder");

// user location status
switch (theUrl) {
    case "/pets/new/":
      locatorContent.innerHTML = "adding a new event";
      break;
    case "/pets/list":
      locatorContent.innerHTML = "seeing the events lists";
      break;
    case "/logout/":
      locatorContent.innerHTML = "leaving the site...";
      break;
    default:
        locatorContent.innerHTML = "editing an event";
  }

