(function() {

    function restorationHeader(btn_menu_obj, remove_class, add_class) {
        btn_menu_obj.removeClass(remove_class);
        btn_menu_obj.addClass(add_class);
    }

    function eventMobileMenu(btn_menu_obj, id_div_display, display_action, remove_class, add_class) {
        $(id_div_display).css("display", display_action);
        restorationHeader(btn_menu_obj, remove_class, add_class);
    }

    function actionHeaderMobile(btn_obj, fa_obj, id_div_display) {
        $(btn_obj).click(function(){
            if(btn_obj == ".btn-menu") {
                $("#mobile-search").css("display", "none");
                restorationHeader($(".btn-search"), "fa-times", "fa-search");
            } else {
                $("#mobile-menu").css("display", "none");
                restorationHeader($(".btn-menu"), "fa-times", "fa-bars");
            }

            if($(this).hasClass(fa_obj)) {
                eventMobileMenu($(this), id_div_display, "block", fa_obj, "fa-times");
            } else {
                eventMobileMenu($(this), id_div_display, "none", "fa-times", fa_obj);
            }
        });
    }

    $(document).ready(function() {
        actionHeaderMobile(".btn-menu", "fa-bars", "#mobile-menu");
        actionHeaderMobile(".btn-search", "fa-search", "#mobile-search");
    });
})($);