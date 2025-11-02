
// --------- Navigation ------------
// Scrolled
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');

    if(window.scrollY > 0){
        navbar.classList.add('scrolled');
    } else{
        navbar.classList.remove('scrolled');
        
    }
});

// Subscription
const navSub = document.querySelector('.nav-sub');
const iconImg = document.getElementById('icon-img');
const text = document.querySelector('.nav-sub-txt h3');
navSub.addEventListener('mouseenter', () => {
  navSub.style.backgroundColor = 'white';
  text.style.color = 'black';
  iconImg.style.backgroundImage = 'url("/Icons/Subscriptions2.png")';
});
navSub.addEventListener('mouseleave', () => {
  navSub.style.backgroundColor = 'transparent';
  text.style.color = 'white';
  iconImg.style.backgroundImage = 'url("/Icons/Subscriptions.png")';
});

// Search
const navsearch = document.querySelector('.nav-search');
const navsericon = document.getElementById('nav-ser-logo');
const navserpopup = document.querySelector('.ser-popup');

let isSerPopupVisible = false;

// Hover
function serShowHover(){
    if(!isSerPopupVisible){
        navsearch.style.backgroundColor = 'white';
        navsericon.style.backgroundImage = 'url(/Icons/search2.png)'
    }
}
function serHideHover(){
    if(!isSerPopupVisible){
        navsearch.style.backgroundColor = 'transparent';
        navsericon.style.backgroundImage = 'url(/Icons/search.png)'
    }
}
navsearch.addEventListener('mouseenter', serShowHover);
navsearch.addEventListener('mouseleave', serHideHover);

// Toggle popup on search click (open/close)
function serShowPopup(){
    isSerPopupVisible = true;
    navsearch.style.backgroundColor = 'white';
    navserpopup.classList.add('serShow');
    main.classList.add('popup-active')
    navsericon.style.backgroundImage = 'url(/Icons/search2.png)'
}
function serHidePopup(){
    isSerPopupVisible = false;
    navsearch.style.backgroundColor = 'transparent';
    navserpopup.classList.remove('serShow');
    main.classList.remove('popup-active');
    navsericon.style.backgroundImage = 'url(/Icons/search.png)'
}
navsearch.addEventListener('click', (e)=>{
    e.stopPropagation();
    if(isSerPopupVisible){
        serHideHover();
    } else{
        serShowPopup();
    }
});
navserpopup.addEventListener('click', (e) =>{
    e.stopPropagation();
});
document.addEventListener('click', (e) =>{
    if(isSerPopupVisible && !navsearch.contains(e.target) && !navserpopup.contains(e.target)){
        serHidePopup();
    }
});


// Language
const navlan = document.querySelector('.nav-lan');
const navlanicon = document.getElementById('lan-img');
const navlanpopup = document.querySelector('.lan-popup');

let isHoveringNavlan = false;
let isHoveringPopuplan = false;

function lanShowPopup() {
    navlan.classList.add('active');
    navlanpopup.classList.add('lanShow');
    navlan.style.backgroundColor = 'white';
    navlan.style.color = 'black';
    navlanicon.style.backgroundImage = 'url(/Icons/dropdown2.png)';
}
function lanHidePopup() {
    navlan.classList.remove('active');
    navlanpopup.classList.remove('lanShow');
    navlan.style.backgroundColor = 'transparent';
    navlan.style.color = 'white';
    navlanicon.style.backgroundImage = 'url(/Icons/dropdown.png)';
}

navlan.addEventListener('mouseenter', () =>{
    isHoveringNavlan = true;
    lanShowPopup();
})
navlan.addEventListener('mouseleave', ()=>{
    isHoveringNavlan = false;
    setTimeout(() =>{
        if(!isHoveringPopuplan){
            lanHidePopup();
        }
    }, 200);
});
navlanpopup.addEventListener('mouseenter', () =>{
    isHoveringPopuplan = true;
    lanShowPopup();
});
navlanpopup.addEventListener('mouseleave', () =>{
    isHoveringPopuplan = false;
    setTimeout(() =>{
        if(!isHoveringNavlan){
            lanHidePopup();
        }
    }, 200);
});


// Multipleselect
const mulsel = document.querySelector('.nav-mul-sel');
const mulselicon = document.getElementById('mulsel-img');
const mulselpopup = document.querySelector('.mulsel-popup')

let isHoveringNavmul = false;
let isHoveringPopupmul = false;

function mulShowpopup(){
    mulsel.style.backgroundColor = 'white';;
    mulselpopup.classList.add('mulShow');
    mulselicon.style.backgroundImage = 'url(/Icons/mutliselector2.png)'
}
function mulHidepopup(){
    mulsel.style.backgroundColor = 'transparent';
    mulselpopup.classList.remove('mulShow');
    mulselicon.style.backgroundImage = 'url(/Icons/mutliselector.png)'
}

mulsel.addEventListener('mouseenter', () =>{
    isHoveringNavmul = true;
    mulShowpopup();
});
mulsel.addEventListener('mouseleave', () =>{
    isHoveringNavmul = false;
    setTimeout(() => {
        if(!isHoveringPopupmul){
            mulHidepopup();
        }
    }, 200);
});
mulselpopup.addEventListener('mouseenter', () =>{
    isHoveringPopupmul = true;
    mulShowpopup();
});
mulselpopup.addEventListener('mouseleave', () =>{
    isHoveringPopupmul = false;
    setTimeout(() => {
        if(!isHoveringNavmul){
            mulHidepopup();
        }
    }, 200);
});


// Account
const navacc = document.querySelector('.nav-acc');
const accPopup = document.querySelector('.acc-popup');

let isHoveringNavacc = false;
let isHoveringPopupacc = false;

function accShowpopup(){
    accPopup.classList.add('accShow');
}
function accHidepopup(){
    accPopup.classList.remove('accShow');
}

navacc.addEventListener('mouseenter', () =>{
    isHoveringNavacc = true;
    accShowpopup();
});
navacc.addEventListener('mouseleave', () =>{
    isHoveringNavacc = false;
    setTimeout(() => {
        if(!isHoveringPopupacc){
            accHidepopup();
        }
    }, 200);
});
accPopup.addEventListener('mouseenter', () =>{
    isHoveringPopupacc = true;
    accShowpopup();
});
accPopup.addEventListener('mouseleave', () =>{
    isHoveringPopupacc = false;
    setTimeout(() => {
        if(!isHoveringNavacc){
            accHidepopup();
        }
    }, 200);
})