$(function(){
    $("#modal-edit-socials").modal('hide')
    // Show modal on button click
    $("#btn-edit-social-links").on("click", ()=>{
        $("#modal-edit-socials").modal('show')
    })

    $("#btn-cancel-update").on("click", ()=>{
        location.reload()
    })

    $("#btn-change-profile").on("click", ()=>{
        $("#modal-change-profile").modal('show')
    })

    $("#id_profile_pic").on("change", (event)=>{
        $("#profile-pic-img").attr('src', URL.createObjectURL(event.target.files[0]))
    })
})