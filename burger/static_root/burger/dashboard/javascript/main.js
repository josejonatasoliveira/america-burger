(function($) {
  "use strict"; // Start of use strict


  // nav
    $(document).ready(function() {
      $("#top-nav-list").metisMenu();
       var $this = $('#top-nav-list'), resizeTimer, self = this;    
      var initCollapse = function(el) {
        if ($(window).width() >= 768) {
          this.find('li').has('ul').children('a').off('click');
        }
      }
      // $(window).resize(function() {
      //     clearTimeout(resizeTimer);
      //     resizeTimer = setTimeout(self.initCollapse($this), 250);
      // });  


      // search
       $("#searchs").click(function() {
            $(".main-wrap").toggleClass('move');
            $("#search-container").toggleClass('opacity-on');
            $(".page").toggleClass('overflow-x');
        });
        $("#search-close").click(function() {
            $(".main-wrap").removeClass('move')
            $("#search-container").toggleClass('opacity-on');
            $(".page").toggleClass('overflow-x');
        });
    });
    // end nav
    $(document).ready(function() {
        $('.notification-close').click(function() {
            $('.notification').hide(1000);
            /* Act on the event */
        });
        $('.drawer').click(function() {
            $('.notification').show(1000);
        });
    });
    // loader
          setTimeout(function(){
            $('body').addClass('loaded');
           
          }, 500);
    // end loader

   $('.dropdown').on('show.bs.dropdown', function(e){
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
  });

  // ADD SLIDEUP ANIMATION TO DROPDOWN //
  $('.dropdown').on('hide.bs.dropdown', function(e){
    
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp(500, function(){
        $('.dropdown').removeClass('open');
        $('.dropdown').find('.dropdown-toggle').attr('aria-expanded','false');
    });
    
  });

   window.FontAwesomeConfig = {
        searchPseudoElements: true
    }



})(jQuery); // End of use strict