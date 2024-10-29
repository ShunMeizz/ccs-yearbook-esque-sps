$(function(){
    $('.edit-comment-form').hide();
    $('.btn-edit-comment').on('click', function(event){
        event.preventDefault();
        let commentID = event.target.value
        $(`#comment-body-${commentID}`).toggle();
        $(`#edit-comment-form-${commentID}`).toggle();

        if ($(`#edit-comment-form-${commentID}`).is(':visible')){
            $(this).text('· Cancel Edit')
        } else {
            $(this).text('· Edit')
            $(`#edit-comment-form-${commentID} textarea`).val()
        }

        console.log($(`#comment-body-${commentID}`).text())
    })
})