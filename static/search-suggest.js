import Fuse from 'https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.mjs'

// const options = [
//     {
//         "name": "6N",
//         "link": "/group/6N"
//     },
//     {
//         "name": "5N",
//         "link": "/group/5N"
//     },
//     {
//         "name": "6N / inz",
//         "link": "/group/6N/inz"
//     },
//     {
//         "name": "Witold Obloza",
//         "link": "/teacher/WO"
//     },
//     {
//         "name": "Warszawa",
//         "link": "/classroom/warszawa"
//     }
// ]
const options = await (await fetch('/api/search_index')).json();




function showSuggestions(options, suggestionsContainer) {
    suggestionsContainer.innerHTML = '';
    let i = 0;
    options.forEach(suboption => {
        if (i >= 5) return;
        const option = suboption.item;
        const li = document.createElement('li');
        li.classList.add('search-suggestions-element');
        li.innerHTML = `<a href="${option.link}">${option.name}</a>`;
        suggestionsContainer.appendChild(li);
        i++;
    })
}

function makeSuggestions(searchField, suggestionsContainer) {
    const fuse = new Fuse(options, {
        keys: ['name']
    });
    const result = fuse.search(searchField.value);
    console.log(result);
    showSuggestions(result, suggestionsContainer);
}
function hideSuggestions(event, suggestionsContainer) {
    console.log(event)
    if (suggestionsContainer.contains(event.relatedTarget)){
        return;
    }
    suggestionsContainer.style.display = 'none';
}

function unhideSuggestions(suggestionsContainer) {
    suggestionsContainer.style.display = 'unset';
}

document.querySelectorAll('.search-suggestions-wrap').forEach(element => {
    const searchField = element.querySelector('.search-field');
    const suggestionsContainer = element.querySelector('.search-suggestions-box');

    searchField.addEventListener('keyup', function() {makeSuggestions(searchField, suggestionsContainer);});
    searchField.addEventListener('focus', function() {unhideSuggestions(suggestionsContainer);});
    searchField.addEventListener('blur', function(event) {hideSuggestions(event, suggestionsContainer);});



});


