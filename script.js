// This script handles the collapsible navigation sections and potentially other custom behaviors.

document.addEventListener('DOMContentLoaded', () => {
    // --- Collapsible Navigation ---
    const collapsibleToggles = document.querySelectorAll('.collapsible-toggle');
    const collapsibleLis = document.querySelectorAll('.collapsible');
    const navLinks = document.querySelectorAll('.navigation-pane a[data-chapter]');

    // Restore expanded sections from localStorage
    const expandedSections = JSON.parse(localStorage.getItem('tocExpanded') || '[]');
    expandedSections.forEach(idx => {
        if (collapsibleLis[idx]) {
            collapsibleLis[idx].classList.add('expanded');
        }
    });

    // Restore selected chapter from localStorage
    const selectedChapter = localStorage.getItem('selectedChapter');
    let restored = false;
    if (selectedChapter) {
        const selectedLink = document.querySelector(`.navigation-pane a[data-chapter="${selectedChapter}"]`);
        if (selectedLink) {
            navLinks.forEach(l => l.classList.remove('active'));
            selectedLink.classList.add('active');
            // Load the chapter content
            if (typeof loadChapterContent === 'function') {
                document.getElementById('chapter-content').dataset.currentChapter = selectedChapter;
                loadChapterContent(selectedChapter);
                restored = true;
            }
        }
    }

    // Only load default chapter if nothing is selected/restored
    if (!restored) {
        if (typeof loadChapterContent === 'function') {
            document.getElementById('chapter-content').dataset.currentChapter = 'kapitola1_uvod.html';
            loadChapterContent('kapitola1_uvod.html');
        }
    }

    // Add a click event listener to each toggle
    collapsibleToggles.forEach((toggle, idx) => {
        toggle.addEventListener('click', () => {
            const li = toggle.parentElement;
            li.classList.toggle('expanded');
            // Save expanded sections
            const expanded = [];
            collapsibleLis.forEach((li, i) => {
                if (li.classList.contains('expanded')) expanded.push(i);
            });
            localStorage.setItem('tocExpanded', JSON.stringify(expanded));
        });
    });

    // Save selected chapter on click
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            localStorage.setItem('selectedChapter', link.getAttribute('data-chapter'));
        });
    });

    // --- Other Custom Scripts ---
    // Add any other custom JavaScript logic here, inside the DOMContentLoaded listener.

});
