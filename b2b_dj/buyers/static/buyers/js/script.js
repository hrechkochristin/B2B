document.addEventListener('DOMContentLoaded', () => {
    // 1. Логіка степперів (Плюс/Мінус)
    const stepperContainers = document.querySelectorAll('.stepper_buyer');
    stepperContainers.forEach(container => {
        const minusBtn = container.querySelector('.minus');
        const plusBtn = container.querySelector('.plus');
        const input = container.querySelector('.stepper-input');

        minusBtn.addEventListener('click', () => {
            let value = parseInt(input.value);
            if (value > parseInt(input.min)) {
                input.value = value - 1;
            }
        });

        plusBtn.addEventListener('click', () => {
            let value = parseInt(input.value);
            input.value = value + 1;
        });
    });

    // 2. Логіка додавання в кошик через AJAX
    document.querySelectorAll('.btn-buy_buyer').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const card = this.closest('.product-card');
            const productId = card.getAttribute('data-product-id');
            const quantity = card.querySelector('.stepper-input').value;
            // Отримуємо ціну з data-атрибута або очищуємо текст
            const priceElement = card.querySelector('.product-price');
            const price = priceElement.getAttribute('data-raw-price') || priceElement.innerText.replace(/[^\d.]/g, '');

            const formData = new FormData();
            formData.append('productId', productId);
            formData.append('quantity', quantity);
            formData.append('price', price);

            fetch(window.location.href, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const cartCount = document.querySelector('.cart-count');
                    if (cartCount) {
                        cartCount.textContent = data.new_count;
                    }
                    // Ефект успішного додавання (опціонально)
                    this.innerText = 'Додано!';
                    this.style.backgroundColor = '#28a745';
                    setTimeout(() => {
                        this.innerText = 'Додати';
                        this.style.backgroundColor = '';
                    }, 2000);
                } else {
                    alert('Помилка: ' + (data.error || 'невідома помилка'));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Сталася помилка при відправці запиту');
            });
        });
    });
});

// Функція для отримання CSRF токена
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}