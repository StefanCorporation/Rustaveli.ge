const logoImage = document.getElementById('logo-image');
const hoverText = document.getElementById('hover-text');

logoImage.addEventListener('mouseover', () => {
    hoverText.textContent = '';
});

logoImage.addEventListener('mouseout', () => {
    hoverText.textContent = '';
});
