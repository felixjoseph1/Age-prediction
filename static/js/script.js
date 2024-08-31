document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        const ageResult = document.getElementById('age-result');
        ageResult.innerHTML = `<p>Predicted Age: ${result.age}</p>`;
        ageResult.parentElement.style.display = 'block';  // Show prediction results
    });
});
