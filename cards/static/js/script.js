document.addEventListener("DOMContentLoaded", function() { //checks that the html page is loaded or not
    const form = document.getElementById('modalformidcheck');
    // const errorbox = document.getElementById('error-box');
    const passform=document.getElementById('passwordchange')

    const modal = document.getElementById('myModal');
    // const successbox = document.getElementById('success-box');

    const imageinput = document.getElementById('id_image');
    const imagepreview = document.getElementById('image-preview'); 
    
    if (imageinput && imagepreview) {
        imageinput.addEventListener('change', function(event) {
            const file = event.target.files[0];

            if (file) {
                imagepreview.src = URL.createObjectURL(file);
            }
        });
    }

    // const forms=document.querySelectorAll('.needs-validation')
    
    passform.addEventListener('submit',async function(event){//event listner of passform for submit 
        event.preventDefault()

        const url=passform.action

        const passformdata=new FormData(passform)
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        document.querySelectorAll('span[id$="_error"]').forEach(span=>span.innerHTML="")
        passform.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));

        
        const response=await fetch(url,{
            method:'POST',
            headers:{
                'X-CSRFToken': csrfToken
            },
            body:passformdata
        })

        const data=await response.json()

        // console.log(data.errors)

        if(response.ok && data.status==="success"){
            alert("Password Changed !!!")
            window.location.reload()
        } else { 
            for (let field in data.errors) {
                let errorspan=document.getElementById(`${field}_error`)
                let inputtag=document.querySelector(`input[name="${field}"]`)
                if (errorspan){
                errorspan.innerHTML=data.errors[field].join("<br>");
                errorspan.style.color="red"
                }
                if (inputtag){
                    inputtag.classList.add("is-invalid")
                }
            }
        }
    })
    form.addEventListener('submit', async function(event) {
        event.preventDefault(); 
        
        // if (!form.checkValidity()){
        //     event.stopPropagation()
            
        //     form.classList.add("was-validated")
        //    Array.from(form.elements).forEach(input=>{
        //         if(!input.validity.valid){
        //             input.classList.add("is-invalid")
        //         }
        //         else{
        //             input.classList.remove("is-invalid")
        //         }
        //     })
        // }
        // errorbox.innerHTML = ""; 
        // successbox.innerHTML = "";
        const url = form.action;
        const formData = new FormData(form);
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        document.querySelectorAll('span[id$="_error"]').forEach(span => span.innerHTML = "");
        form.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        });
        
        const data = await response.json(); 

        if (response.ok && data.status === 'success') { 
            // successbox.innerHTML = '<p>Saved Successfully !!!</p>';

            alert("Saved Successfuly!!!")
            window.location.reload()
        } else { 
            for (let field in data.errors) {
                let errorspan=document.getElementById(`${field}_error`)
                let inputtag=document.querySelector(`input[name="${field}"]`)

                if (errorspan){
                errorspan.innerHTML=data.errors[field].join("<br>");
                errorspan.style.color="red"
                }
                if (inputtag){
                    inputtag.classList.add("is-invalid")
                }
                modal.scrollTop = 0; 
            }
        }
        modal.scrollTop = 0; 
        
        
    });
});

