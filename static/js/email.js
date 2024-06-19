function Contact() {
    var tempParams = {
        from_name:document.getElementById("from_name").value,
        from_email:document.getElementById("from_email").value,
        message:document.getElementById("message").value,
    };

    emailjs.send('service_xx2o104','template_6yopv7a',tempParams)
    .then(function(res){
        document.getElementById(".modal-confirm").classList.add("active");
        console.log("success", res.status);
    })
}