// Toggle dropdown menu
        const profileDropdown = document.getElementById('profileDropdown');
        const dropdownMenu = profileDropdown.querySelector('.dropdown-menu');

        profileDropdown.addEventListener('click', (e) => {
            dropdownMenu.classList.toggle('active');
            e.stopPropagation();
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (!profileDropdown.contains(e.target)) {
                dropdownMenu.classList.remove('active');
            }
        });