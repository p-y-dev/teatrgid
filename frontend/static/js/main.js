(function() {

    function eventMobileMenu(btn_menu_obj, display_action, remove_class, add_class) {
        $("#mobile-menu").css("display", display_action);
        btn_menu_obj.removeClass(remove_class);
        btn_menu_obj.addClass(add_class);
    }

    function actionMobileMenu() {
        $(".btn-menu").click(function(){
            if($(this).hasClass("fa-bars")) {
                eventMobileMenu($(this), "block", "fa-bars", "fa-times");
            } else {
                eventMobileMenu($(this), "none", "fa-times", "fa-bars");
            }
        });
    }

    $(document).ready(function() {
        actionMobileMenu();
    });
})($);