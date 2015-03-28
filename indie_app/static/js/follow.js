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
     *  Subscribe Follow
     *
     */

       $.ajax({
            type: "GET",
            url: link,
            success: function(r) {
                console.log(r);
                if (r.status == "ok") {
                    if ($('.brand_follow').find('span').hasClass('follow')) {
                              //str.replace(regexp, newSubStr|function)
                              link.replace('subscribe', 'unsubscribe');
                              $('.brand_follow').attr('href', link)
                        $('.brand_follow').find('span').removeClass('follow')
                        $('.brand_follow').find('span').addClass('unfollow')
                    } else {
                        link.replace('subscribe', 'unsubscribe');
                              $('.brand_follow').attr('href', link)
                        $('.brand_follow').find('span').removeClass('unfollow')
                        $('.brand_follow').find('span').addClass('follow')
                    }

                } else {
                    console.error(r.error);
                }
            }
        });
    });
/*

    $('.brand_follow').click(function(e) {
    	
    	e.preventDefault();
    	alert('followed...');

    	var link = $('.brand_follow').attr('href');

    	link += '&ajax=1';
		alert(link);
		
		$.ajax({
		    type: "GET",
		    url: link,
		    success: function(r) {
		        console.log(r);
		        if (r.status == "ok") {
		        	if ($(this).find('span').hasClass('follow')) {
		        	          //str.replace(regexp, newSubStr|function)
		        	          link.replace('subscribe', 'unsubscribe');
		        	          $('.brand_follow').attr('href', link)
                        $(this).find('span').removeClass('follow')
                        $(this).find('span').addClass('unfollow')
                    } else {
                        link.replace('subscribe', 'unsubscribe');
		        	          $('.brand_follow').attr('href', link)
                        $(this).find('span').removeClass('unfollow')
                        $(this).find('span').addClass('follow')
                    }

		        } else {
		            console.error(r.error);
		        }
		    }
		});
    });
*/
});
