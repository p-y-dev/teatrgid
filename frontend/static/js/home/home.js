(function() {
    function openFilter() {
        $("#open-filter").click(function(){
            var filter_obj = $(".filter");
            var btn_open_obj = $("#open-filter");

            if(filter_obj.hasClass("open")) {
                filter_obj.removeClass("open");
                filter_obj.css("display", "none");
                btn_open_obj.text("Открыть фильтр");
            } else {
                filter_obj.css("display", "block");
                filter_obj.addClass("open");
                btn_open_obj.text("Закрыть фильтр");
            }
        })
    }

    $(document).ready(function() {
        openFilter();
    });
})($);