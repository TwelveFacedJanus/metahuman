document.getElementById('themeToggle').addEventListener('click', function(e) {
    e.preventDefault();
    

    const isDark = document.body.classList.toggle('dark-theme');
    document.body.classList.toggle('light-theme', !isDark);

    const buttons = document.querySelectorAll('.theme-switch-btn');
    
    buttons.forEach(btn => {
        if (isDark) {
  
            btn.classList.remove('btn-dark');
            btn.classList.add('btn-light');
        } else {

            btn.classList.remove('btn-light');
            btn.classList.add('btn-dark');
        }
    });
});