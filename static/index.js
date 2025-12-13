function toggleDropdownMenu() {
    const elements = document.getElementsByClassName("nav-link");
    if (document.getElementsByClassName("search-box")[0].style.display === "none") {
        document.getElementsByClassName("search-box")[0].removeAttribute("style");
        for (let i = 0; i < elements.length; i++) {
            elements[i].removeAttribute("style");
        }
    } else {
        document.getElementsByClassName("search-box")[0].style.display = "none";
        for (let j = 0; j < elements.length; j++) {
            elements[j].style.setProperty("display", "none");
        }
    }
}

function hideMessage() {
    document.getElementById('notification-message').style.display = 'none';
}