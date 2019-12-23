$(document).ready(function(){
            $(".mobile-utilities").hide();

     $(".mobile-menu-items").hide()
    $(".show-footer").click(function () {

        $(".mobile-utilities").show()
    })
     $(".mobile-menu-icon").click(function () {
       $(".mobile-menu-items").show('slow')
    })
});