//************* Template Button **************
let btnMyTemplate = document.querySelector('#btn-my-template');
let btnMyCommunity = document.querySelector('#btn-my-community');
let displayMyTemp = document.querySelector('.in-active-5');
let displayCorporateTemp = document.querySelector('.in-active-8');
let btnCorporate = document.querySelector('.btn-corporate');
let btnCorporateComm = document.querySelector('#corporate-comm');
let btnCorporateTemp = document.querySelector('#corporate-temp');
let sdAgrementLink = document.querySelector('#sd-agreement');
let displayCorpTempList = document.querySelector('.in-active-9');
let btnCorpTempCancel = document.querySelector('.btn-temp-cancel');


//************* Create Insight **************

let btnAddInsight = document.querySelectorAll('.btn-create-insight');
let btnCancelInsight = document.querySelector('#btn-cancel');
let displayCreateInsight = document.querySelector('.in-active-7');


//************* Modal Button **************
let displaySaveModal = document.querySelector('.in-active-modal');
let btnModalCancel = document.querySelector('#modal-btn-cancel');
let btnModalWithInsight = document.querySelector('#modal-btn-with-insight');
let btnModalWithoutInsight = document.querySelector('#modal-btn-without-insight');
let btnModalWithTemp = document.querySelector('#modal-btn-as-template');
let displayCreateTemplateII = document.querySelector('.in-active-10');
let displayModalWithTemp = document.querySelector('.in-active-11');
let displayCreateTemplate = document.querySelector('.in-active-12');
let btnSaveTempCancel = document.querySelector('.btn-save-temp-cancel');
let btnUploadTempCancel = document.querySelector('#btn-upload-cancel');
let btnUploadTemp = document.querySelector('#btn-upload-temp');
let btnSaveTempFinish = document.querySelector('.btn-save-temp-finish');
let btnTempCategories = document.querySelectorAll('.create-temp> .cards > .card');



btnTempCategories.forEach( item => {
	item.addEventListener('click', function(){
		displayCreateTemplate.style.display = 'none';
		
	});
});



// TOGGLE SIDEBAR
// let closeSide = document.querySelector('.main');
let menuBar = document.querySelector('.menu');
let sidebar = document.querySelector('.sidebar');

menuBar.addEventListener('click', function () {
    	sidebar.classList.toggle('hide');
    })

menuBar.addEventListener('click', function () {
    	sidebar.style.display = 'block';
    })

// closeSide.addEventListener('click', function () {
//             	sidebar.style.display = 'none';
//             // sidebar.classList.add('hide');
//         })


// const searchButton = document.querySelector('#content nav form .form-input button');
// const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
// const searchForm = document.querySelector('#content nav form');

// searchButton.addEventListener('click', function (e) {
// 	if(window.innerWidth < 576) {
// 		e.preventDefault();
// 		searchForm.classList.toggle('show');
// 		if(searchForm.classList.contains('show')) {
// 			searchButtonIcon.classList.replace('bx-search', 'bx-x');
// 		} else {
// 			searchButtonIcon.classList.replace('bx-x', 'bx-search');
// 		}
// 	}
// })



//************* Document Manager Variables********************
// ***********************************************

// dynamic table Fetch data from doc-manager table database
const table = document.querySelector("#documents");
// let select, index, parties, icon, title, users, statuses, created, insight;

const toDo = `TO DO <i><br><img src="../img/icon/todo.png" alt=""></i>`;
const completed = `Completed <i><br><img src="../img/icon/complete.png" alt=""></i>`;
const addInsight = `<button class="btn-create-insight btn-add-insight">Add <i><img src="../img/icon/add.png" alt=""></i></button>`;
const updated = `<button class="btn-create-insight btn-update-insight">Update <i><img src="../img/icon/update.png" alt=""></i></button> `;




// Upload Profile Pic....
const img = document.querySelectorAll('.display-pic');
const file = document.querySelector('#file');




// User Section Flow 
const manageBtn = document.querySelector('#btn-manage');
const editPwdBtn = document.querySelector('#btn-edit-pwd');
const addBtn = document.querySelector('#btn-add-account');
const arrowBackBtn1 = document.querySelector('#btn-back-arrow1');
const arrowBackBtn = document.querySelector('#btn-back-arrow');
const iconEditImage = document.querySelector('#icon-edit');
const doneUploadBtn = document.querySelector('#btn-done');
const submitPwdBtn = document.querySelector('#btn-pwd-submit');
const pwdDoneBtn = document.querySelector('#btn-pwd-done');


const displayManage = document.querySelector('.in-active');
const displayEditPwd = document.querySelector('.in-active-2');
const displayUpload = document.querySelector('.in-active-3');
const displaySuccessPage = document.querySelector('.in-active-4');


	


// Filter Document Manager with Search

let filterInput = document.getElementById('doc-search');

filterInput.addEventListener('keyup', filterNames);

function filterNames(){
	//filter value
	let filterValue = document.getElementById('doc-search').value.toUpperCase();

	let table = document.getElementById('documents');
	let tr = table.querySelectorAll('tr');

	for(let i = 1; i < tr.length; i++){
		let td = tr[i].querySelectorAll('tr td.file-name')[0];
		if(td.innerHTML.toUpperCase().indexOf(filterValue) > -1){
			tr[i].style.display = '';
		} else {
			tr[i].style.display = 'none';
		}
	}
}


// Filter Document Manager with Date

let filterDate = document.getElementById('date');
let btnDate = document.getElementById('btn-submit');

btnDate.addEventListener('click', filterDate2);

function filterDate2(){
	//filter value
	let filterValue = document.getElementById('date').value.toUpperCase();

	let table = document.getElementById('documents');
	let tr = table.querySelectorAll('tr');

	for(let i = 1; i < tr.length; i++){
		let td = tr[i].querySelectorAll('tr td.file-date')[0];
		if(td.innerHTML.toUpperCase().indexOf(filterValue) > -1){
			tr[i].style.display = '';
		} else {
			tr[i].style.display = 'none';
		}
	}
}






	btnAddInsight.forEach(btnAddIn => {
		btnAddIn.addEventListener('click', displayInsightFunc);
	});
	
	
	
	function displayInsightFunc(){
		displayCreateInsight.style.display = 'block';
		displaySaveModal.style.display = "none";
	}







//************* Document Manager ********************
// ***********************************************

let fileType = document.querySelector("#doc-manager > .form-section > #filetype");
let btnEdit = document.querySelector("#doc-manager> .btn-section >  #btn-edit");

// dynamic table Fetch data from doc-manager table database
// 	for(let i = 0; i <= docIndex.length; i++){
// 		createList(index[i], parties[i], title[i], users[i], date[i], insight[i]);
// 	}


fileType.addEventListener('change', fileSelected);


function fileSelected(){
	if (fileType.value === 'doc') {
		window.location.assign("docmanager")
	} 
	else if (fileType.value === 'pdf')  {
		window.location.assign("pdfmanager")
	}
	else if (fileType.value === 'edit')  {
		window.location.assign("editormanager")
	}
	else if (fileType.value === 'mytemp')  {
		window.location.assign("mytempmanager")
	}
}





function createList (index, parties, title, users, status, date, insight){
    let tr = document.createElement("tr");
    
	let td1 = tr.appendChild(document.createElement("td"));
	let td2 = tr.appendChild(document.createElement("td"));
    let td3 = tr.appendChild(document.createElement("td"));
    let td4 = tr.appendChild(document.createElement("td"));
	let td5 = tr.appendChild(document.createElement("td"));
	let td6 = tr.appendChild(document.createElement("td"));
    let td7 = tr.appendChild(document.createElement("td"));
    let td8 = tr.appendChild(document.createElement("td"));
    let td9 = tr.appendChild(document.createElement("td"));


	td1.innerHTML = `<input type="radio" name="select-file" id="">`;
	td2.innerHTML = index;
	td3.innerHTML = parties;
	td4.innerHTML = `<img src="../img/icon/ms-word.png" alt="">`;
	td5.innerHTML = title;
	td6.innerHTML = users;
	td7.innerHTML = status;
	td8.innerHTML = date;
	td9.innerHTML = insight;

	table.appendChild(tr);
}




//************* Editor Section ********************
// ***********************************************

































//************* Clause Library ********************
// ***********************************************
let btnExpand = document.querySelector('#expand');
let btnClose = document.querySelector('#btn-close');
let displayClauseEditor = document.querySelector('.in-active-6');
let listClauses = document.querySelectorAll('.clause-library > .sidebar-2 > .words > .list > ul > li');
let displayClauses = document.querySelector('#clauses');
let displayClausesHead = document.querySelector('#clauses > h3');
let allClauses = document.querySelector('#all-clause');
let clausesEditors = document.querySelector('.clause-editor');




// **************** Insight **********************
// ***********************************************

// dynamic table Fetch data from Insight Table database
const tableInsight = document.querySelector("#documents-2");
let renewals, titleInsight, partiesInsight, effectiveDate, expiryDate, consideration, liability, term, government;


	// for(let i = 0; i <= docIndex.length; i++){
	// 	createList(renewals[i], titleInsight[i], partiesInsight[i], effectiveDate[i], expiryDate[i], consideration[i], liability[i], term[i], government[i]);
	// }

	// createList2(10, 'My Documents', 'Ayomide, Taofeeq', '10-02-21', '10-10-22', 200, 50000, 4, 'Nigeria');
	// createList2(10, 'My Documents', 'Ayomide, Taofeeq', '10-02-21', '10-10-22', 200, 50000, 4, 'USA');

function createList2 (renewals, titleInsight, partiesInsight, effectiveDate, expiryDate, consideration, liability, term, government){
    let tr = document.createElement("tr");
    
	let td1 = tr.appendChild(document.createElement("td"));
	let td2 = tr.appendChild(document.createElement("td"));
    let td3 = tr.appendChild(document.createElement("td"));
    let td4 = tr.appendChild(document.createElement("td"));
	let td5 = tr.appendChild(document.createElement("td"));
	let td6 = tr.appendChild(document.createElement("td"));
    let td7 = tr.appendChild(document.createElement("td"));
    let td8 = tr.appendChild(document.createElement("td"));
    let td9 = tr.appendChild(document.createElement("td"));
    let td0 = tr.appendChild(document.createElement("td"));


	td1.innerHTML = `<input type="radio" name="select-file" id="">`;
	td2.innerHTML = renewals;
	td3.innerHTML = titleInsight;
	td4.innerHTML = partiesInsight;
	td5.innerHTML = effectiveDate;
	td6.innerHTML = expiryDate;
	td7.innerHTML = consideration;
	td8.innerHTML = liability;
	td9.innerHTML = term;
	td0.innerHTML = government;

	tableInsight.appendChild(tr);
}










//*************  Legal Terminologies *************
// ***********************************************

const readMoreBtn = document.querySelectorAll('.btn-read-more');
// const post = document.querySelectorAll('#legal-terminology > #terms > .item');
const noOfCharacter = 150;
const text = document.querySelectorAll('.text');


text.forEach(content => {

	if(content.textContent.length < noOfCharacter){
		content.nextElementSibling.style.display = 'none';
	}else {
		let displayText = content.textContent.slice(0, noOfCharacter);
		let moreText = content.textContent.slice(noOfCharacter);
		content.innerHTML = `${displayText} <span class='dots'>...</span><span class='hide-text more-text'>${moreText}</span>`;

	}
})


function readMore(btn){
	let post = btn.parentElement;
	post.querySelector(".dots").classList.toggle("hide-text");
	post.querySelector(".more-text").classList.toggle("hide-text");

	btn.textContent == "Read More"? btn.textContent = "Read Less": btn.textContent = "Read More";
}


readMoreBtn.forEach(element => {
	element.addEventListener('click', () =>{
		readMore(element);
	})
});




// for (let i = 0; i < readMoreBtn.length; i++) {
// 	readMoreBtn[i].addEventListener('click', () =>{

		// for (let k = 0; k < text.length; k++) {
		// 	if (i === k) {
		// 		text[k].classList.add('show-more');
		// 		if ( readMoreBtn[i].innerText === 'Read More') {
		// 				readMoreBtn[i].innerText = 'Read Less';
		// 			} 
		// 			else{
		// 				text[k].classList.remove('show-more');
		// 				readMoreBtn[i].innerText = 'Read More';
		// 			}

		// 		} 
			 
		// }
// 	});
	
// }



