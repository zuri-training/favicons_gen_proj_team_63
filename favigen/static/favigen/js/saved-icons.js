const hamburger = document.querySelector(".hambuger");
const navMenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");

})

    // document.querySelectorAll(".a")forEach (n => n.addEventListener("click", () =>{
    //   hamburger.classList.remove("active");
    //   navMenu.classList.remove("active");
    // }))