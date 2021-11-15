window.addEventListener("scroll",()=>{
    const p= window.scrollY;
    console.log(p)
    if(p>=1){
        document.body.classList.add("mast_navbar");
    }
    else if(p==0){
        document.body.classList.remove("mast_navbar");
    }
});


        const navToggle = document.querySelector(".nav-toggle");
        const navLinks = document.querySelectorAll(".nav_link");

        navToggle.addEventListener("click", () => {
            document.body.classList.toggle("nav-open");
        });

        navLinks.forEach((link) => {
            link.addEventListener("click", () => {
                document.body.classList.remove("nav-open");
            });
        });