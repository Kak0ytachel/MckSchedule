function toggleDropdownMenu() {
    if (document.getElementsByClassName("navbar-search-wrap")[0].style.display === "none") {
        showDropDownMenu();
    } else {
        hideDropDownMenu();
    }
}

function showDropDownMenu() {
    const elements = document.getElementsByClassName("nav-link");
    document.getElementsByClassName("navbar-search-wrap")[0].removeAttribute("style");
        for (let i = 0; i < elements.length; i++) {
            elements[i].removeAttribute("style");
        }
}

function hideDropDownMenu() {
    const elements = document.getElementsByClassName("nav-link");
    document.getElementsByClassName("navbar-search-wrap")[0].style.display = "none";
        for (let j = 0; j < elements.length; j++) {
            elements[j].style.setProperty("display", "none");
        }
}

function resizeCheckDropDownMenu() {
    if (window.innerWidth > 500) {
        showDropDownMenu();
    }
}

function hideMessage() {
    document.getElementById('notification-message').style.display = 'none';
}


function getCookieByName(name) {
    // console.log("getCookieByName:")
    // console.log(document.cookie)
     const cookies = document.cookie.split(';');
     for (let cookie of cookies) {
          cookie = cookie.trim();
          if (cookie.startsWith(name + '=')) {
              let result = cookie.substring(name.length + 1);
              // console.log(`result: ${result}`);
              return result;
          }
     }
     // console.log("Cookie not found, returning null")
    return null;
}

// console.log(navigator.language);
addEventListener('resize', resizeCheckDropDownMenu);