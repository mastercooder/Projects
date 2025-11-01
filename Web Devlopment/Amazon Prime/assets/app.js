
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
navsearch.addEventListener('mouseenter', () =>{
    navsearch.style.backgroundColor = 'white';
    navsericon.style.backgroundImage = 'url(/Icons/search2.png)'
});
navsearch.addEventListener('mouseleave', () =>{
    navsearch.style.backgroundColor = 'transparent';
    navsericon.style.backgroundImage = 'url(/Icons/search.png)'
});

// Language
const navlan = document.querySelector('.nav-lan');
const navlanicon = document.getElementById('lan-img');
navlan.addEventListener('mouseenter', () =>{
    navlan.style.backgroundColor = 'white';
    navlan.style.color = 'black';
    navlanicon.style.backgroundImage = 'url(/Icons/dropdown2.png)'
});
navlan.addEventListener('mouseleave', () =>{
    navlan.style.backgroundColor = 'transparent';
    navlan.style.color = 'white';
    navlanicon.style.backgroundImage = 'url(/Icons/dropdown.png)'
});

// Multipleselect
const mulsel = document.querySelector('.nav-mul-sel');
const mulselicon = document.getElementById('mulsel-img');
mulsel.addEventListener('mouseenter', () =>{
    mulsel.style.backgroundColor = 'white';
    mulsel.style.color = 'black';
    mulselicon.style.backgroundImage = 'url(/Icons/mutliselector2.png)'
});
mulselicon.addEventListener('mouseleave', () =>{
    mulsel.style.backgroundColor = 'transparent';
    mulsel.style.color = 'white';
    mulselicon.style.backgroundImage = 'url(/Icons/mutliselector.png)'
});
