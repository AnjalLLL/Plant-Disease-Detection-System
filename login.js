function showModel(){
    document.querySelector('.overlay').classList.add('showoverlay')
    document.querySelector('.login-form').classList.add('showloginform')
}
function closeModel(){
    document.querySelector('.overlay').classList.remove('showoverlay')
    document.querySelector('.login-form').classList.remove('showloginform')
}


document.addEventListener('DOMContentLoaded', function () {
    const togglePassword = document.querySelector('#toggelePassword');
    const passwordInput = document.querySelector('#myInput');

    togglePassword.addEventListener('click', function (e) {
        // Toggle the type attribute
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);

        // Toggle the eye icon
        this.classList.toggle('fa-eye-slash');
    });
    var btnlogin=document.querySelector(".btn-login");
 btnlogin.addEventListener("click",showModel)

 var close=document.querySelector("span");
 close.addEventListener("click",closeModel)
});