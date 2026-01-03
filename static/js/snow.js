document.addEventListener('DOMContentLoaded', function() {
    const snowflakes = document.querySelectorAll('.snowflake');
    snowflakes.forEach(snow => {
        const left = Math.random() * 100;
        const delay = Math.random() * 5;
        const duration = Math.random() * 10 + 5;
        const size = Math.random() * 1.5 + 0.5;

        snow.style.left = `${left}vw`;
        snow.style.animationDelay = `${delay}s`;
        snow.style.animationDuration = `${duration}s`;
        snow.style.fontSize = `${size}em`;
        snow.style.opacity = Math.random() * 0.5 + 0.3;
    });
});
