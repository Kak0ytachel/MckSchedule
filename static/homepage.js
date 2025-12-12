document.addEventListener('DOMContentLoaded', function() {
    const parent = document.getElementById('time-table');
    const children = parent.querySelectorAll('*');

    // Get the initial fixed height defined in CSS/style attribute
    const fixedHeight = parent.offsetHeight;
    let accumulatedHeight = 0;
    let elementsToFit = 0;

    for (let i = 0; i < children.length; i++) {
        const child = children[i];

        // Get the full height of the child element, including margins
        // outerHeight(true) in jQuery is equivalent to offsetHeight + computed margins in pure JS
        const childHeight = child.offsetHeight +
                            parseInt(window.getComputedStyle(child).marginTop) +
                            parseInt(window.getComputedStyle(child).marginBottom);

        // Check if adding this child exceeds the fixed height
        if (accumulatedHeight + childHeight <= fixedHeight) {
            accumulatedHeight += childHeight;
            elementsToFit++;
        } else {
            // Stop when the next element would be cut off
            break;
        }
    }

    // Apply the newly calculated height to the parent
    // This will only include the height of the 'elementsToFit' number of children
    const base = document.getElementById('search')

    if (elementsToFit > 0) {
        base.style.height = accumulatedHeight + 'px';
    } else {
        // Handle case where not even the first element fits, maybe set height to 0 or first child's height
        base.style.height = '0px';
    }
    base.style.color = 'tomato';
});