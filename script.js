// This script handles the collapsible navigation sections.

document.addEventListener('DOMContentLoaded', () => {
    // Find all elements with the class 'collapsible-toggle'
    const collapsibleToggles = document.querySelectorAll('.collapsible-toggle');

    // Add a click event listener to each toggle
    collapsibleToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            // Find the parent list item (li) and toggle the 'expanded' class
            toggle.parentElement.classList.toggle('expanded');
        });
    });
});
