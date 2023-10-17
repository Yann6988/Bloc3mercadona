window.onload = () => {
    let filters = document.querySelectorAll("#filters div");

    for(let filter of filters){
        filter.addEventListener("click", function(){
            let tag = this.id;
            console.log(tag);
            let produits = document.querySelectorAll('.category');

            for (let produit of produits){
                produit.classList.replace("active", "inactive");

                if(tag in produit.dataset || tag === "all"){
                    produit.classList.replace("inactive","active")
                }
            }
        });
    }
}

let filters = document.querySelectorAll("#filtersmobile div");

for(let filter of filters){
    filter.addEventListener("click", function(){
        let tag = this.id;
        console.log(tag);
        let produits = document.querySelectorAll('.category');

        for (let produit of produits){
            produit.classList.replace("active", "inactive");

            if(tag in produit.dataset || tag === "all"){
                produit.classList.replace("inactive","active")
            }
        }
    });
}



function toggler(){
    const menu = document.querySelector('#filtersmobile');
    const icon = document.querySelector("#toggler");

    if (icon.innerHTML == "menu"){

        icon.innerHTML = "close";
        menu.style.transform= "translateX(0%)";
    }
    else {
        icon.innerHTML = "menu";
        menu.style.transform= "translateX(-100%)";
    }
}




