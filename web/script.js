/* =========================================
   FAQ ACCORDION
========================================= */

const faqItems = document.querySelectorAll(".faq-item");

faqItems.forEach((item) => {

    const question = item.querySelector(".faq-question");

    question.addEventListener("click", () => {

        /*
         * Ferme les autres questions
         */
        faqItems.forEach((otherItem) => {

            if (otherItem !== item) {
                otherItem.classList.remove("active");
            }

        });


        /*
         * Ouvre / ferme la question sélectionnée
         */
        item.classList.toggle("active");

    });

});


/* =========================================
   BOUTON COMMENCER
========================================= */

const startButton = document.getElementById("startButton");

startButton.addEventListener("click", () => {

    document.querySelector(".faq-section").scrollIntoView({
        behavior: "smooth"
    });

});