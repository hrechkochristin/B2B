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