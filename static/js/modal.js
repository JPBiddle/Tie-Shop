// Variables

// Open modal button 
const openModalButtons = document.querySelectorAll('[data-modal-target]');
// Close modal button 
const closeModalButtons = document.querySelectorAll("[data-close-button]");

//add event listeners for modal buttons//
openModalButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const modal = document.querySelector(button.dataset.modalTarget);
        openModal(modal);
    });
});

//Close button on modal//
closeModalButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const modal = button.closest(".modal-confirm");
        closeModal(modal);
    });
});

//Open function for modal//

function openModal(modal) {
    if (modal == null) return;
    modal.classList.add("active");
    overlay.classList.add("active");
}

//Close function for modal//

function closeModal(modal) {
    if (modal == null) return;
    modal.classList.remove("active");
    overlay.classList.remove("active");
}

// Click off modal to close

overlay.addEventListener("click", () => {
    const modals = document.querySelectorAll(".modal-confirm.active");
    modals.forEach(modal => {
        closeModal(modal);
    });
});