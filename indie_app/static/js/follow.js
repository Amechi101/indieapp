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
                        $(this).find('span').removeClass('follow')
                        $(this).find('span').addClass('unfollow')
                    } else {
                        $(this).find('span').removeClass('unfollow')
                        $(this).find('span').addClass('follow')
                    }

		        } else {
		            console.error(r.error);
		        }
		    }
		});
    });

});
