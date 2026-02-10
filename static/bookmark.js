
// handles bookmark icon click event
function bookmarkClick(event) {
    // console.log(event.target)
    let bookmark = event.target;

    let items = JSON.parse(getCookieByName("bookmarks"))
    if (items === null) {
        items = []
    }

    let link = window.location.pathname;
    if (link.includes("/semester/")) {
        link = link.split("/semester/")[0]
    }

    let title = document.querySelector("#schedule-title")
    let item = {"name": title.getAttribute("data-title"), "link": link}

    if (bookmark.getAttribute("data-is-saved") === "true") {
        // unsave
        bookmark.setAttribute("data-is-saved", "false");
        bookmark.src = bookmark.getAttribute("data-src-empty");

        for (let i = 0; i < items.length; i++) {
            if (items[i].name === item.name) {
                items.splice(i, 1);
                break;
            }
        }
        showSnackbar("Unsaved schedule")
    } else {
        // save
        bookmark.setAttribute("data-is-saved", "true");
        bookmark.src = bookmark.getAttribute("data-src-filled");

        let exists = false;
        for (let i = 0; i < items.length; i++) {
            if (items[i].name === item.name) {
                exists = true;
                break;
            }
        }
        if (exists) {
            console.log("Warning: item already exists in bookmarks");
        } else {
            items.push(item);
        }
        showSnackbar("Saved schedule")
    }
    console.log(items);
    let now = Date.now();
    let expires = new Date(now + 365 * 24 * 60 * 60 * 1000);
    document.cookie = "bookmarks=" + JSON.stringify(items) + "; expires=" + expires.toUTCString() + "; path=/;";
    // document.cookie = "bookmarks=" + JSON.stringify(items) + "; path=/;";
    // console.log(document.cookie);
}

// loads bookmark icon state when page loads
function bookmarkInit() {
    let items = JSON.parse(getCookieByName("bookmarks"))
    let bookmark = document.querySelector("#bookmark")

    let name = document.querySelector("#schedule-title").getAttribute("data-title")

    let isSaved = false;
    for (let i = 0; i < items.length; i++) {
        if (items[i].name === name) {
            isSaved = true;
            break;
        }
    }
    if (isSaved) {
        bookmark.setAttribute("data-is-saved", "true")
        bookmark.src = bookmark.getAttribute("data-src-filled")
    }
}

let snackbarTimer;

function showSnackbar(message) {
    console.log(`Showing snackbar: ${message}`)
    const x = document.getElementById("snackbar");
    clearTimeout(snackbarTimer);
    x.innerText = message;

    x.classList.remove("show-snackbar");

    // Trigger reflow:
    // Accessing offsetWidth forces the browser to re-render the
    // element without the 'show' class immediately.
    void x.offsetWidth;

    x.classList.add("show-snackbar");

    snackbarTimer = setTimeout(function() {
        x.classList.remove("show-snackbar");
    }, 3000);
}

window.addEventListener('load', bookmarkInit);