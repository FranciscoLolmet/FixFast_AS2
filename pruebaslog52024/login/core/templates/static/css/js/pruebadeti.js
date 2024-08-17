document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('ticketForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Validate form fields
        const title = document.getElementById('title').value.trim();
        const description = document.getElementById('description').value.trim();
        const priority = document.getElementById('priority').value.trim();

        if (!title || !description || !priority) {
            alert('Please fill in all fields');
            return;
        }

        // Simulate sending data to server (replace with actual AJAX request)
        setTimeout(function() {
            alert('Ticket created successfully');
            form.reset(); // Reset form fields
        }, 1000);
    });
});
