$(function () {
    $(window).on('load', function(){
        $('.preloader').delay(50).fadeOut('slow', function(){
        	$(this).attr('style', 'display: none !important');
        });
    });

	baguetteBox.run('.gallery', {
    animation: 'fadeIn',
    noScrollbars: true
});


	 $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.arrow_page_up').fadeIn();
        } else {
            $('.arrow_page_up').fadeOut();
        }
    });

    $('.arrow_page_up').click(function () {
        $('html, body').animate({scrollTop: 0}, 800);
        return false;
    });
})