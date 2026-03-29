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