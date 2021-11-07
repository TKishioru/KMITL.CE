jQuery(document).ready(function($){
    //open popup
    $('.cd-popup-notify').on('click', function(event){
        event.preventDefault();
        $('#notifyConfirm').addClass('visible');
        $('.cd-popup').addClass('is-visible');
    });
    $('.cd-popup-delete').on('click', function(event){
        event.preventDefault();
        $('#deleteConfirm').addClass('visible');
        $('.cd-popup').addClass('is-visible');
    });
    
    //close popup
    $('.cd-popup').on('click', function(event){
        if( $(event.target).is('.cd-popup-close') || $(event.target).is('.cd-popup') ) {
            event.preventDefault();
            $('#notifyConfirm').removeClass('visible');
            $('#deleteConfirm').removeClass('visible');
            $(this).removeClass('is-visible');
        }
    });
});