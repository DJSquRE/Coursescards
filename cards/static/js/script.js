document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('modalformidcheck');
    const errorBox = document.getElementById('error-box');

    form.addEventListener('submit', async function(event) {

        event.preventDefault(); 
        
        errorBox.innerHTML = ""; 

        const url = form.action;
        const formData = new FormData(form);
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken
                },
                body: formData
            });

            const data = await response.json(); 

            if (response.ok && data.status === 'success') { 
                window.location.reload(); 
            } else { 
                for (let field in data.errors) {
                    for(let i=0;i<data.errors[field].length;i++)
                        errorBox.innerHTML += `<p> > ${data.errors[field][i]}</p>`;
                        
                }
            }
        
    });
});