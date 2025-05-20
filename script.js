// This script handles the collapsible navigation sections and potentially other custom behaviors.

document.addEventListener('DOMContentLoaded', () => {
    // --- Collapsible Navigation ---
    // Find all elements with the class 'collapsible-toggle'
    const collapsibleToggles = document.querySelectorAll('.collapsible-toggle');

    // Add a click event listener to each toggle
    collapsibleToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            // Find the parent list item (li) and toggle the 'expanded' class
            toggle.parentElement.classList.toggle('expanded');
        });
    });

    // --- Other Custom Scripts ---
    // Add any other custom JavaScript logic here, inside the DOMContentLoaded listener.

});
