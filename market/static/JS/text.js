const logoImage = document.getElementById('logo-image');
const hoverText = document.getElementById('hover-text');

logoImage.addEventListener('mouseover', () => {
    hoverText.textContent = 'Shota Rustaveli';
});

logoImage.addEventListener('mouseout', () => {
    hoverText.textContent = 'Shota Rustaveli';
});
