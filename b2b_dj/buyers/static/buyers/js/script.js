document.addEventListener("DOMContentLoaded", () => {
    // =========================
    // Stepper + / -
    // =========================
    document.querySelectorAll(".stepper_buyer").forEach((stepper) => {
        const minusBtn = stepper.querySelector(".minus");
        const plusBtn = stepper.querySelector(".plus");
        const input = stepper.querySelector(".stepper-input");

        if (!minusBtn || !plusBtn || !input) return;

        minusBtn.addEventListener("click", () => {
            let currentValue = parseInt(input.value, 10) || 1;
            const minValue = parseInt(input.min, 10) || 1;

            if (currentValue > minValue) {
                input.value = currentValue - 1;
            }
        });

        plusBtn.addEventListener("click", () => {
            let currentValue = parseInt(input.value, 10) || 1;
            input.value = currentValue + 1;
        });

        input.addEventListener("input", () => {
            let currentValue = parseInt(input.value, 10);
            const minValue = parseInt(input.min, 10) || 1;

            if (isNaN(currentValue) || currentValue < minValue) {
                input.value = minValue;
            }
        });

        input.addEventListener("blur", () => {
            let currentValue = parseInt(input.value, 10);
            const minValue = parseInt(input.min, 10) || 1;

            if (isNaN(currentValue) || currentValue < minValue) {
                input.value = minValue;
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const cartModal = document.getElementById("cartModal");
    const floatingCartBtn = document.getElementById("floatingCartBtn");
    const closeModalBtn = document.querySelector(".modal-close");
    const body = document.body;

    // Функція відкриття
    const openCart = () => {
        cartModal.style.display = "block";
        body.classList.add("modal-open"); // Блокуємо скрол фону
    };

    // Функція закриття
    const closeCart = () => {
        cartModal.style.display = "none";
        body.classList.remove("modal-open"); // Повертаємо скрол фону
    };

    // Слухачі подій
    if (floatingCartBtn) {
        floatingCartBtn.addEventListener("click", openCart);
    }

    if (closeModalBtn) {
        closeModalBtn.addEventListener("click", closeCart);
    }

    // Закриття при кліку поза межами модалки (на темний фон)
    window.addEventListener("click", (e) => {
        if (e.target === cartModal) {
            closeCart();
        }
    });

    // Опціонально: закриття клавішею Escape
    document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && cartModal.style.display === "block") {
            closeCart();
        }
    });
});
