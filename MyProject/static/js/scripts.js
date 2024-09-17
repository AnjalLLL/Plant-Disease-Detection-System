// Handle Login Form Submission
document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Get form values
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    // Simulate form validation or submission
    if (email && password) {
        alert('Login Successful!');

        // Close the modal after login
        $('#loginModal').modal('hide');
    } else {
        alert('Please fill in all the fields.');
    }
});

// Handle Signup Form Submission
document.getElementById('signupForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Get form values
    const name = document.getElementById('signupName').value;
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;

    // Simulate form validation or submission
    if (name && email && password) {
        alert('Signup Successful!');

        // Close the modal after signup
        $('#signupModal').modal('hide');
    } else {
        alert('Please fill in all the fields.');
    }
});