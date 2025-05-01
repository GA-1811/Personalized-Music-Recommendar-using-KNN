// Update slider value displays
document.getElementById('danceability').addEventListener('input', function() {
    document.getElementById('danceValue').textContent = this.value;
});

document.getElementById('energy').addEventListener('input', function() {
    document.getElementById('energyValue').textContent = this.value;
});

document.getElementById('valence').addEventListener('input', function() {
    document.getElementById('valenceValue').textContent = this.value;
});