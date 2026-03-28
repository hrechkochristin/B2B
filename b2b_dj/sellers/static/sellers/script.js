const modal = document.getElementById('productModal');
const openBtn = document.querySelector('.btn-add-product');
const closeBtn = document.querySelector('.close-button');
const form = document.getElementById('productForm');

// Відкрити / Закрити
openBtn.onclick = () => modal.style.display = 'block';
closeBtn.onclick = () => modal.style.display = 'none';
window.onclick = (e) => { if (e.target == modal) modal.style.display = 'none'; };

// Обробка форми
form.onsubmit = function(e) {
    e.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    
    // Окремо збираємо масиви чекбоксів
    data.features = formData.getAll('features');
    data.temp_range = formData.getAll('temp_range');

    console.log('Дані товару готові до відправки:', data);
    alert('Товар успішно додано (див. консоль)');
    
    form.reset();
    modal.style.display = 'none';
};