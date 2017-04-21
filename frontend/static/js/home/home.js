(function() {
    function activateChangePerformances(id_top_div, count_top_block, time_change, id_blocks_change, class_block_change) {
        if($("div").is(id_top_div) && count_top_block > 1) {
            changePerformances(
                time_change,
                count_top_block,
                id_blocks_change,
                class_block_change
            );
        }
    }

    function changePerformances(time, count_top_block, id_blocks_change, class_block_change) {
        var i = 0;
        $(class_block_change).addClass("hide-performance");
        $(id_blocks_change + i).removeClass("hide-performance");
        i++;
        setInterval(function() {
            if(i == count_top_block) i = 0;
            $(class_block_change).addClass("hide-performance");
            $(id_blocks_change + i).removeClass("hide-performance");
            i++;
        }, time);
    }

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
        var is_top_today_perf = ".is-top-today-perf";
        var is_top_week_ahead_perf = ".is-top-week-ahead-perf";
        var div_top = $("div");

        var count_top_block = $(is_top_today_perf).data("count");
        if(div_top.is(is_top_today_perf) && count_top_block > 1) {
            activateChangePerformances(
                is_top_today_perf,
                count_top_block,
                time_change = 3000,
                "#top-today-perf-",
                ".top-tody-performance"
            );
        }

        count_top_block = $(is_top_week_ahead_perf).data("count");
        if(div_top.is(is_top_week_ahead_perf) && count_top_block > 1) {
            activateChangePerformances(
                is_top_week_ahead_perf,
                count_top_block,
                time_change=6000,
                "#top-week-ahead-perf-",
                ".top-week-ahead-performance"
            );
        }

        openFilter();
    });
})($);