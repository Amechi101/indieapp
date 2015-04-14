$(document).ready(function(){

	/*
     *
     *  Login Follow
     *
     */

    $('.brand_login_follow').on('click', function( event ) {
        
        event.preventDefault();

        var _this = $(this);

        $.ajax({
            type: "GET",
            success : function(data) {
                $('#ajax-login-brand').load(_this.data('url'));
            }
        });
    });

    /*
     *
     *  Subscribe/Unsubscribe Follow
     *
     */

    var link = $('.brand_follow').attr('href');
        link += '&ajax=1';

    $('.brand_follow').click(function ( event ) {
    	var brandFollow = $('.brand_follow').find('div').hasClass('follow');
    	
        event.preventDefault();

      $.ajax({
            type: "GET",
            url: link,
            success: function( data ) {
                if (data.status == "ok") {
                    if ( brandFollow ) {

                        link = link.replace('unsubscribe', 'subscribe');
                        
                        $('.brand_follow').attr('href', link);
                        $('.brand_follow').find('div').removeClass('follow');
                        $('.brand_follow').find('div').addClass('unfollow');


                    } else {
                        link = link.replace('subscribe', 'unsubscribe');
                        
                        $('.brand_follow').attr('href', link);
                        $('.brand_follow').find('div').removeClass('unfollow');
                        $('.brand_follow').find('div').addClass('follow');
                    }

                } else {
                    console.error(data.error);
                }
            }
        });
    });
});

