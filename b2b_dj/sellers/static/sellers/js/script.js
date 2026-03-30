document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('productModal');
    const openBtn = document.querySelector('.btn-add-product');
    const closeBtn = document.querySelector('.close-button');
    const form = document.getElementById('productForm');

    if (openBtn) {
        openBtn.onclick = () => {
            modal.style.display = 'block';
        };
    }

    if (closeBtn) {
        closeBtn.onclick = () => {
            modal.style.display = 'none';
        };
    }

    window.onclick = (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };

    const noControl = document.querySelector('input[value="no_control"]');
    const tempCheckboxes = document.querySelectorAll('input[name="temp_range"]:not([value="no_control"])');

    if (noControl) {
        noControl.addEventListener('change', function () {
            if (this.checked) {
                tempCheckboxes.forEach(cb => cb.checked = false);
            }
        });

        tempCheckboxes.forEach(cb => {
            cb.addEventListener('change', function () {
                if (this.checked) {
                    noControl.checked = false;
                }
            });
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const orders = document.querySelectorAll('.order-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const filter = button.dataset.filter;

            // Активна кнопка
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            orders.forEach(order => {
                const statusElement = order.querySelector('.order-status');

                if (!statusElement) return;

                const statusClasses = statusElement.classList;

                if (filter === 'all') {
                    order.style.display = 'block';
                } else {
                    if (statusClasses.contains(filter)) {
                        order.style.display = 'block';
                    } else {
                        order.style.display = 'none';
                    }
                }
            });
        });
    });
});