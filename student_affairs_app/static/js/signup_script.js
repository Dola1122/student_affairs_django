
console.log("signup.js")
const signupForm = document.querySelector('.user-data-form');
const usernameInput = document.getElementById('username');
const phoneInput = document.getElementById('phone');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');

signupForm.addEventListener('submit', (event) => {
  if (usernameInput.value.trim() === '') {
    event.preventDefault(); 
    alert('Please enter a username.');
    usernameInput.focus(); 
    return;
  }

  if (phoneInput.value.trim() === '' || !isValidPhoneNumber(phoneInput.value)) {
    event.preventDefault();
    alert('Please enter a valid phone number.');
    phoneInput.focus(); 
    return;
  }

  if (emailInput.value.trim() === '' || !isValidEmail(emailInput.value)) {
    event.preventDefault(); 
    alert('Please enter a valid email address.');
    emailInput.focus(); 
    return;
  }

  if (passwordInput.value.trim() === '' || passwordInput.value.length < 8) {
    event.preventDefault(); 
    alert('Please enter a password that is at least 8 characters long.');
    passwordInput.focus();
    return;
  }
});

function isValidPhoneNumber(phone) {
    console.log("josdkfjjsdfjkasjdfhijadf");
    const phoneRegex = /(01)[0125][0-9]{8}/;
    // return phone.match(phoneRegex)
    console.log(phoneRegex.test(phone));
    return phoneRegex.test(phone);
}

// Helper function to validate email addresses
function isValidEmail(email) {
  // TODO: Implement email validation
  return true;
}
