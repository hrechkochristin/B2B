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