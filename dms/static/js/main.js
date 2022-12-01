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

btnUploadTemp.addEventListener('click', function(){
		displayCreateTemplateII.style.display = "none";   //c
		displayCreateTemplate.style.display = 'block';
	});

btnUploadTempCancel.addEventListener('click', function(){
		displayModalWithTemp.style.display = 'block';
		displayCreateTemplateII.style.display = 'none';
	});

	btnSaveTempFinish.addEventListener('click', function(){
		displayModalWithTemp.style.display = 'none';
		displayCreateTemplateII.style.display = 'block';
	});
	
	
	btnSaveTempCancel.addEventListener('click', function(){
		displaySaveModal.style.display = "block";
	displayModalWithTemp.style.display = "none";
});



btnModalWithTemp.addEventListener('click', function(){
	displayModalWithTemp.style.display = 'block';
	displaySaveModal.style.display = "none";
	tabcontent[5].style.display = "block";
	tablinks[5].classList.add("active");
	tablinks[0].classList.remove("active");
});


btnModalWithInsight.addEventListener('click', clickedDocManagerInsight);


function clickedDocManagerInsight(){
	tabcontent[2].style.display = "block";
	tablinks[2].classList.add("active");
	tabcontent[0].style.display = "none";
	tablinks[0].classList.remove("active");
	displayCreateInsight.style.display = 'block';
	displaySaveModal.style.display = "none";
}


const btnSave = document.querySelector("#btn-save-editor");

btnSave.addEventListener('click', function(){
	displaySaveModal.style.display = "block";
});





btnModalCancel.addEventListener('click', function(){
	displayCreateTemplateII.style.display = "none"; //c
	displaySaveModal.style.display = "none";
});





// let displayNextForm = document.querySelector('.saveas2');
// let btnCorpTempPrev = document.querySelector('.btn-temp-prev');
// let btnCorpTempNext = document.querySelector('.btn-temp-next');


// let btnNewTemplate = document.querySelector('#btn-new-template');





// Sidebar / Tab Section 
let tabcontent = document.getElementsByClassName("tabcontent");
let tablinks = document.getElementsByClassName("tablinks");
let gotoEditor = document.getElementById('goto-doc-editor');
let gotoTemplate = document.getElementById('goto-template');
let btnWithoutInsight = document.getElementById('modal-btn-without-insight');

let btnWithInsight = document.getElementById('modal-btn-with-insight');


gotoEditor.addEventListener('click', clickedEditor);
gotoTemplate.addEventListener('click', clickedTemplate);
btnWithoutInsight.addEventListener('click', clickedDocManager);

function clickedEditor(){
tabcontent[3].style.display = "block";
tablinks[3].classList.add("active");
tablinks[0].classList.remove("active");
}
function clickedTemplate(){
tabcontent[5].style.display = "block";
tablinks[5].classList.add("active");
tablinks[0].classList.remove("active");
}

function clickedDocManager(){
	tabcontent[2].style.display = "block";
	tablinks[2].classList.add("active");
	tabcontent[0].style.display = "none";
	tablinks[0].classList.remove("active");
	displaySaveModal.style.display = "none";
}


function openTab(evt, tab) {
    // let tablinks;
    for (let i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tab).style.display = "block";
    evt.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();



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

file.addEventListener('change', function(){
	const chooseFile = this.files[0];

	if (chooseFile){
		const reader = new FileReader();
		reader.addEventListener('load', function(){
			for(let i = 0; i <= img.length; i++){
				img[i].setAttribute('src', reader.result);
			}
		} );

		reader.readAsDataURL(chooseFile);
	}
});




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


// const displayManage = document.querySelector('.in-active');
// const displayEditPwd = document.querySelector('.in-active-2');
// const displayUpload = document.querySelector('.in-active-3');
const displaySuccessPage = document.querySelector('.in-active-4');



// Controls Upload Profile Picture Screen 
// iconEditImage.addEventListener('click', function(){
// 		displayUpload.style.display = 'block';
// 	});

// doneUploadBtn.addEventListener('click', function(){
// 			displayUpload.style.display = 'none';
// 		});


// Controls Manage User Screen 
// manageBtn.addEventListener('click', function(){
// 		displayManage.style.display = 'block';
// 	});
	
// arrowBackBtn1.addEventListener('click', function(){
// 		displayManage.style.display = 'none';
// });


// Controls Change Password Screen
// editPwdBtn.addEventListener('click', function(){
// 		displayManage.style.display = 'none';
// 		displayEditPwd.style.display = 'block';
// 	});

// submitPwdBtn.addEventListener('click', function(){
// 		displayEditPwd.style.display = 'none';
// 		displaySuccessPage.style.display = 'block';
// 	});


// pwdDoneBtn.addEventListener('click', function(){
// 		displaySuccessPage.style.display = 'none';
// 	});
	
// returns to previous screen
// arrowBackBtn.addEventListener('click', function(){
// 		displayEditPwd.style.display = 'none';
// 		displayManage.style.display = 'block';

// });
	


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

btnCancelInsight.addEventListener('click', function(){
			displayCreateInsight.style.display = 'none';
			
		});





//************* Document Manager ********************
// ***********************************************


// dynamic table Fetch data from doc-manager table database
// 	for(let i = 0; i <= docIndex.length; i++){
// 		createList(index[i], parties[i], title[i], users[i], date[i], insight[i]);
// 	}


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






listClauses.forEach( item => {
	item.addEventListener('click', function(){
		let list = item.innerText;
		displayClausesHead.innerText = list;
		displayClauses.style.display = 'block';
	});
});

allClauses.addEventListener('click', function(){
	displayClauses.style.display = 'none';
});

clausesEditors.addEventListener('click', function(){
	displayClauses.style.display = 'none';
});



btnExpand.addEventListener('click', function(){
	btnClose.style.display = 'inline-block';
	displayClauseEditor.style.display = 'block';
	btnExpand.style.display ='none';
	
});

btnClose.addEventListener('click', function(){
	displayClauseEditor.style.display = 'none';
	btnExpand.style.display ='inline-block';
	btnClose.style.display = 'none';
});


// Filter Clause Library 
let filterInputClause = document.getElementById('clause-search');

filterInputClause.addEventListener('keyup', filterNames1);

function filterNames1(){
	//filter value
	let filterValue = document.getElementById('clause-search').value.toUpperCase();

	let list = document.querySelector('.list');

	let li = list.querySelectorAll('ul li');

	for(let i = 0; i < li.length; i++){
		 let a = li[i];
		if(a.innerHTML.toUpperCase().indexOf(filterValue) > -1){
			li[i].style.display = '';
		} else {
			li[i].style.display = 'none';
		}
	}
}


let inputSearch = document.getElementById('input-search');

inputSearch.addEventListener('keyup', filterNames2);

function filterNames2(){
	//filter value
	let filterValue = document.getElementById('input-search').value.toUpperCase();
	let clause = document.querySelector('.clause');
	
	let item = clause.querySelectorAll('.item');
	
	for(let i = 0; i < item.length; i++){
		let h3 = item[i].querySelectorAll('.item h3')[0];

		if(h3.innerHTML.toUpperCase().indexOf(filterValue) > -1){
			item[i].style.display = '';
		} else {
			item[i].style.display = 'none';
		}
	}
}













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






// Legal Terminology 
let termSearch = document.getElementById('term-search');

termSearch.addEventListener('keyup', filterNames3);

function filterNames3(){
	//filter value
	let filterValue = document.getElementById('term-search').value.toUpperCase();
	let clause = document.querySelector('#terms');
	
	let item = clause.querySelectorAll('#terms .item');
	
	for(let i = 0; i < item.length; i++){
		let h3 = item[i].querySelectorAll('.item h3')[0];

		if(h3.innerHTML.toUpperCase().indexOf(filterValue) > -1){
			item[i].style.display = '';
		} else {
			item[i].style.display = 'none';
		}
	}
}








//*************  Notification ********************
// ***********************************************

// Filter Notification 
let notifySearch = document.getElementById('search-notify');

notifySearch.addEventListener('keyup', filterNamesNotify);

function filterNamesNotify(){
	//filter value
	let filterValue = document.getElementById('search-notify').value.toUpperCase();
	let clause = document.querySelector('.notificate');
	
	let item = clause.querySelectorAll('.note');
	
	for(let i = 0; i < item.length; i++){
		let h3 = item[i].querySelectorAll('.item .content h3')[0];

		if(h3.innerHTML.toUpperCase().indexOf(filterValue) > -1){
			item[i].style.display = '';
		} else {
			item[i].style.display = 'none';
		}
	}
}








// btnCorpTempNext.addEventListener('click', function(){
// 	displayNextForm.style.display = 'block';
// });

// btnCorpTempPrev.addEventListener('click', function(){
// 	displayNextForm.style.display = 'none';
// });



// sdAgrementLink.addEventListener('click', function(){
// 	displayCorpTempList.style.display = 'block';
// });
// btnCorpTempCancel.addEventListener('click', function(){
// 	displayNextForm.style.display = 'none';``
// 	displayCorpTempList.style.display = 'none';
// });


btnMyTemplate.addEventListener('click', function(){
	displayMyTemp.style.display = 'block';
});
btnMyCommunity.addEventListener('click', function(){
	displayMyTemp.style.display = 'none';
});
btnCorporate.addEventListener('click', function(){
	displayCorporateTemp.style.display = 'block';
});
btnCorporateTemp.addEventListener('click', function(){
	displayCorporateTemp.style.display = 'none';
});
btnCorporateComm.addEventListener('click', function(){
	displayCorporateTemp.style.display = 'none';
	displayMyTemp.style.display = 'none';
});


// Community File Search 
let fileComSearch = document.getElementById('file-search-comTemp');

fileComSearch.addEventListener('keyup', filterNames5);

function filterNames5(){
	//filter value
	let filterValue = document.getElementById('file-search-comTemp').value.toUpperCase();
	let file = document.querySelector('.comm-cards');
	
	let card = file.querySelectorAll('.comm-cards .card');
	
	for(let i = 0; i < card.length; i++){
		let p = card[i].querySelectorAll('.card p')[0];
		
		if(p.innerHTML.toUpperCase().indexOf(filterValue) > -1){
			card[i].style.display = '';
		} else {
			card[i].style.display = 'none';
		}
	}
}


// My Template File Search 
let fileSearch = document.getElementById('file-search-myTemp');

fileSearch.addEventListener('keyup', filterNames6);

function filterNames6(){
	//filter value
	let filterValue = document.getElementById('file-search-myTemp').value.toUpperCase();
	let file = document.querySelector('.mytemp-cards');
	
	let card = file.querySelectorAll('.mytemp-cards .card-1');
	
	for(let i = 0; i < card.length; i++){
		let p = card[i].querySelectorAll('.card-1 p')[0];
		
		if(p.innerHTML.toUpperCase().indexOf(filterValue) > -1){
			card[i].style.display = '';
		} else {
			card[i].style.display = 'none';
		}
	}
}

// ************* Create New Template *************
// ***********************************************

// dynamic creation of my Template
const tempCards = document.querySelector(".mytemp-cards");


function createTemplateFolder ( img, ptag, nclass){
    let aTag = document.createElement("a");
    aTag.classList.add('card-1');
	let divTag = aTag.appendChild(document.createElement("div"));
	divTag.classList.add('new-div');
	divTag.innerHTML = `<img style = "width : 90px; margin: 30px;" src="../img/icon/${img}" alt="homeimage" srcset=""> <p>${ptag}</p>`
	
	tempCards.appendChild(aTag);
}

createTemplateFolder('folder.png', 'New Document');










