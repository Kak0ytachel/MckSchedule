const languageChangeDialog = document.querySelector('.language-menu');
const languageDialogButton = document.querySelector('.language-menu-open-button');

// opens and closes the language menu
window.addEventListener('click', (event) => {

    // console.log(dialog.style.display, event.target);
    if (!languageChangeDialog.contains(event.target) && languageChangeDialog.style.display !== 'none') {
        languageChangeDialog.style.display = 'none';
    } else if (languageChangeDialog.style.display === 'none' && languageDialogButton === event.target)
    {
        // console.log('show');
        languageChangeDialog.style.display = 'block';
    }
    else if (languageChangeDialog.style.display === 'block' && event.target === languageDialogButton)
    {
        // console.log('hide');
        languageChangeDialog.style.display = 'none';
    }


});


let bookmarkMenuButton = document.querySelector('.saved-menu-open-button');
let bookmarkMenu = document.querySelector('.saved-menu-box');
let bookmarkMenuEmpty = document.querySelector('.saved-menu-empty');

// preloads saved menu items
function showSavedMenu() {
    let items = JSON.parse(getCookieByName('bookmarks')) ?? [];
    let names = items.map(item => item['name']);
    let names_there = []
    // console.log(items);
    // console.log(bookmarkMenuEmpty);
    for (let i = 0; i < bookmarkMenu.children.length; i++) {
        let child = bookmarkMenu.children[i]
        if (child.classList.contains('saved-menu-empty')) {
            // console.log("its there!")
            continue;
        }
        if (names.includes(child.innerText)) {
            names_there.push(child.innerText);
            continue;
        }
        child.remove();
        i--;
    }
    for (let item of items) {
        if (names_there.includes(item.name)) continue;
        let a = document.createElement('a');
        a.classList.add('saved-menu-button');
        a.href = item.link;
        a.innerText = item.name;
        bookmarkMenu.appendChild(a)
    }

    if (bookmarkMenu.children.length === 1) {
        bookmarkMenuEmpty.style.display = 'block';
    } else {
        bookmarkMenuEmpty.style.display = 'none';
    }

}

bookmarkMenuButton.addEventListener('click', showSavedMenu);

const savedChangeDialog = document.querySelector('.saved-menu');
const savedDialogButton = document.querySelector('.saved-menu-open-button');


// opens and closes the saved menu
window.addEventListener('click', (event) => {

    // console.log(dialog.style.display, event.target);
    if (!savedChangeDialog.contains(event.target) && savedChangeDialog.style.display !== 'none') {
        savedChangeDialog.style.display = 'none';
    } else if (savedChangeDialog.style.display === 'none' && savedDialogButton === event.target)
    {
        // console.log('show');
        savedChangeDialog.style.display = 'block';
    }
    else if (savedChangeDialog.style.display === 'block' && event.target === savedDialogButton)
    {
        // console.log('hide');
        savedChangeDialog.style.display = 'none';
    }


});