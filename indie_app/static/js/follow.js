$(document).ready(function(){

    $('#unlabelFollow').click(function(e) {
       e.preventDefault();
      alert('followed...');
      // <a id="unlabelFollow" href="/account/api/subscribe/?brand_name={{ brand.brand_name }}"><span class=" brand-follow icon-unlabel_web-05"></span></a>
      var link = $('#unlabelFollow').attr('href');
      alert(link);
      $.ajax({
            type: "GET",
            url: link,
            success: function(r) {
                alert(r);
                if (r.status == "ok") {
                } else {
                    alert(r.error);
                }
            }
        });
    }
});
