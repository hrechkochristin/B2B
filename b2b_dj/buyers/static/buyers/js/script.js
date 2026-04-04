// buyers.js

// =========================
// 1. Підключення Supabase
// =========================
const supabaseUrl = "https://YOUR_PROJECT.supabase.co";
const supabaseKey = "PUBLIC_ANON_KEY"; // заміни на свій
const supabase = supabase.createClient(supabaseUrl, supabaseKey);

// =========================
// 2. Stepper + / -
// =========================
document.querySelectorAll('.stepper_buyer').forEach(stepper => {
    const minusBtn = stepper.querySelector('.minus');
    const plusBtn = stepper.querySelector('.plus');
    const input = stepper.querySelector('.stepper-input');

    minusBtn.addEventListener('click', () => {
        let val = parseInt(input.value);
        if (val > parseInt(input.min)) input.value = val - 1;
    });

    plusBtn.addEventListener('click', () => {
        input.value = parseInt(input.value) + 1;
    });
});

// =========================
// 3. Додавання в кошик
// =========================
document.querySelectorAll('.product-card').forEach(form => {
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const product_id = form.querySelector('input[name="product_id"]').value;
        const quantity = parseInt(form.querySelector('input[name="quantity"]').value);
        const unit = form.querySelector('select[name="unit"]').value;
        const user_id = 1; // заміни на реальний ID користувача або з auth

        try {
            const { data, error } = await supabase
                .from('cart_items')
                .insert([
                    {
                        product_id: product_id,
                        user_id: user_id,
                        quantity: quantity,
                        unit: unit
                    }
                ]);

            if (error) {
                console.error('Помилка при додаванні в кошик:', error);
                alert('Помилка при додаванні товару!');
            } else {
                console.log('Товар додано в кошик:', data);
                alert('Товар додано в кошик!');
                // тут можна додати оновлення лічильника у шапці
            }
        } catch (err) {
            console.error(err);
            alert('Помилка мережі!');
        }
    });
});