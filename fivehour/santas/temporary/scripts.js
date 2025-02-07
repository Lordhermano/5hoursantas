// Function to show the selected content
function showContent(index) {
    // Get all content items
    const contentItems = document.querySelectorAll('.content-item');
    
    // Hide all content items
    contentItems.forEach((item) => {
        item.classList.remove('active');
    });

    // Show the content for the selected index
    const selectedContent = document.getElementById(`content-${index}`);
    selectedContent.classList.add('active');
}

// Initialize the first tab as active
document.addEventListener('DOMContentLoaded', () => {
    showContent(0); // Default show content for Tab 1
});
