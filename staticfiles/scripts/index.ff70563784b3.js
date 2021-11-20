console.log('we here');


$('.elipses__bg').click(function(){
    $('.update-popup__bg').addClass('active');
    $(this).addClass('active');
})

$('a[crud-popup-cancel]').click(function(){
    $('.update-popup__bg').removeClass('active');
    $('.elipses__bg').removeClass('active');
})