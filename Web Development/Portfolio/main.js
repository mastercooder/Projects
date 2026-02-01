/* --------------------Loding Screen-------------------- */
const loadingScreen = document.getElementById("loading-screen");
const mainIcon = document.querySelector(".main-icon");
const loadingText = document.getElementById("loading-text");
const subIcons = document.querySelectorAll(".sub-icons i");
const designerText = document.getElementById("designer-text");

// Helper Funtion to show element with delay          
function showElement(element, delay = 0){
    setTimeout(() =>{
        element.classList.remove("hidden");
        element.classList.add("fall");
    }, delay);
}
0
// Run animation when page loads
document.addEventListener("DOMContentLoaded", ()=>{
    showElement(loadingText, 0);
    showElement(mainIcon, 800);

    subIcons.forEach((icon, index) =>{
        showElement(icon, 1600 + index * 400);
    });
    showElement(designerText, 2800);

    // Remove loading screen
    setTimeout(() =>{
        loadingScreen.style.opacity = "0";
        setTimeout(() =>{
            loadingScreen.style.display = "none";
        }, 500);
    }, 4000);
});