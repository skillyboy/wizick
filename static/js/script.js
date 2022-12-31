// Signup Section 
const pwd_1 = document.querySelector("#create-pwd");
const pwd_2 = document.querySelector("#confirm-pwd");
const errorText = document.querySelector('.error-text'); 
const btnCreateAccount = document.querySelector("#btn-create-acct");
const btnShow = document.querySelector(".show");


pwd_1.addEventListener('keyup', active);

function active(){
	
	if(pwd_1.value.length >= 6){
		btnCreateAccount.removeAttribute("disabled", "");
		btnCreateAccount.classList.add("active");
		pwd_2.removeAttribute("disabled", "");
	}else{
		btnCreateAccount.setAttribute("disabled", "");
		btnCreateAccount.classList.remove("active");
		pwd_2.setAttribute("disabled", "");
	}
}

btnCreateAccount.addEventListener('click', confirmPassword);

function confirmPassword(){
	if(pwd_1.value != pwd_2.value){
		errorText.style.display = 'block';
		errorText.textContent = "Error! Confirm Password Not Matched";
		errorText.classList.remove("matched");
	} else{
		errorText.style.display = 'block';
		errorText.classList.add("matched");
		errorText.textContent = "Nice! Confirm Password Matched";
	}

	
}

pwd_2.addEventListener('keyup', active2);

function active2(){
	if(pwd_2.value != ""){
		btnShow.style.display = "block"
		btnShow.addEventListener('click', viewPassword);
	}else{
		btnShow.style.display = "none"

	}
}


function viewPassword(){
	if( (pwd_1.type == "password") && (pwd_2.type == "password") ){
		pwd_1.type = "text";
		pwd_2.type = "text";
		this.textContent = "Hide";
		this.classList.add("active");
	} else {
		pwd_1.type = "password";
		pwd_2.type = "password";
		this.textContent = "Show";
		this.classList.remove("active");
	}
}







