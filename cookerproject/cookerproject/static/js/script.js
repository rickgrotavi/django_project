function show_comments_form(parent_comment_id){
    if(parent_comment_id == 'write_comment')
    {
        $("#id_parent_comment").val('');
    }
    else
    {
        $("#id_parent_comment").val(parent_comment_id);
    }
    $("#comment_form").insertAfter("#"+parent_comment_id);
}

$(function() {
    function onNavbar() {
      if (window.innerWidth >= 768) {
        $('.navbar-default .dropdown').on('mouseover', function(){
          $('.dropdown-toggle', this).next('.dropdown-menu').show();
        }).on('mouseout', function(){
          $('.dropdown-toggle', this).next('.dropdown-menu').hide();
        });
        $('.dropdown-toggle').click(function() {
          if ($(this).next('.dropdown-menu').is(':visible')) {
            window.location = $(this).attr('href');
          }
        });
      } else {
        $('.navbar-default .dropdown').off('mouseover').off('mouseout');
      }
    }
    $(window).resize(function() {
      onNavbar();
    });
    onNavbar();
  



    $(".navbar-collapse a").click(function() {
      if (!$(this).hasClass("dropdown-toggle")) {
        $(".navbar-collapse").collapse('hide');
      }
    });
  });