document.addEventListener('DOMContentLoaded', () => {
    // 1. Конфігурація (ЗАМІНИ НА СВОЇ ДАНІ З SUPABASE DASHBOARD)
    const SUPABASE_URL = 'https://xehsouorkbtvtpegsqya.supabase.co'; 
    const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhlaHNvdW9ya2J0dnRwZWdzcXlhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ0Njk0NTIsImV4cCI6MjA5MDA0NTQ1Mn0.4X9rsF6b0YPHIMfzO4Ma7r1ilRV71vz33-L55A_B3OU'; // Візьми його в Settings -> API
    const TABLE_NAME = 'products_product'; // Назва таблиці, яку ти створив у Supabase (наприклад, 'products')

    // 2. Пошук елементів
    const modal = document.getElementById('productModal');
    const openBtn = document.querySelector('.btn-add-product');
    const closeBtn = document.querySelector('.close-button');
    const form = document.getElementById('productForm');

    // --- ЛОГІКА ВІДКРИТТЯ/ЗАКРИТТЯ ---

    if (openBtn) {
        openBtn.onclick = () => {
            modal.style.display = 'block';
        };
    } else {
        console.error("Кнопка '.btn-add-product' не знайдена!");
    }

    closeBtn.onclick = () => modal.style.display = 'none';

    window.onclick = (event) => {
        if (event.target === modal) modal.style.display = 'none';
    };

    // --- ЛОГІКА РОБОТИ ЧЕКБОКСІВ (Взаємовиключення) ---

    const noControl = document.querySelector('input[value="no_control"]');
    const tempCheckboxes = document.querySelectorAll('input[name="temp_range"]:not([value="no_control"])');

    if (noControl) {
        noControl.addEventListener('change', function() {
            if (this.checked) tempCheckboxes.forEach(cb => cb.checked = false);
        });

        tempCheckboxes.forEach(cb => {
            cb.addEventListener('change', function() {
                if (this.checked) noControl.checked = false;
            });
        });
    }

    // --- ВІДПРАВКА ДАНИХ У SUPABASE ---

    form.onsubmit = async function(e) {
        e.preventDefault();

        // Збираємо дані з форми
        const formData = new FormData(form);
        
        // Створюємо об'єкт для бази
        const productData = {
            name: formData.get('productName'),
            category: formData.get('productCategory'),
            price: parseFloat(formData.get('productPrice')) || 0,
            stock: parseInt(formData.get('productStock')) || 0,
            weight: parseFloat(formData.get('productWeight')) || 0,
            volume: parseFloat(formData.get('productVolume')) || 0,
            // features: formData.getAll('features'), // Масив
            temperature_regime: formData.getAll('temp_range'), // Масив
            description: formData.get('productDescription')
        };

        try {
            const response = await fetch(`${SUPABASE_URL}/rest/v1/${TABLE_NAME}`, {
                method: 'POST',
                headers: {
                    'apikey': SUPABASE_KEY,
                    'Authorization': `Bearer ${SUPABASE_KEY}`,
                    'Content-Type': 'application/json',
                    'Prefer': 'return=minimal'
                },
                body: JSON.stringify(productData)
            });

            if (response.ok) {
                alert('Товар успішно додано до бази!');
                form.reset();
                modal.style.display = 'none';
            } else {
                const errData = await response.json();
                console.error('Помилка Supabase:', errData);
                alert('Помилка: ' + (errData.message || 'Невідома помилка'));
            }
        } catch (error) {
            console.error('Помилка мережі:', error);
            alert('Не вдалося з’єднатися з базою даних.');
        }
    };
});
