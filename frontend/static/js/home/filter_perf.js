var filter_data = {};

function filterPerformances(filter_data) {
    $(".preloader-performance").css("display", "block");
    $.ajax({
        url: "/filter_performances/",
        type: "POST",
        dataType: 'json',
        data: {
            "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]:first").val(),
            "filter_data": JSON.stringify(filter_data),
        },

        success: function (data) {
            $(".preloader-performance").css("display", "none");

            if (data["status"] === "success") {
                $('.row-performances').html(data["filtered_data"]);
            }
        },

        error: function () {
            $(".preloader-performance").css("display", "none");
        }
    });
}

function addValueFilter(value) {
    var name_filter_data = 0;
    var value_filter_data = 1;
    var json_data = value.split("=");

    switch (json_data[name_filter_data]) {
        case "date":
            filter_data.date = json_data[value_filter_data];
            break;

        case "rating":
            filter_data.rating = json_data[value_filter_data];
            break;

        case "age-from":
            filter_data.age_from = json_data[value_filter_data];
            break;

        case "age-to":
            filter_data.age_to = json_data[value_filter_data];
            break;

        case "theaters":
            filter_data.theaters = json_data[value_filter_data];
            break;

        case "genres":
            filter_data.genres = json_data[value_filter_data];
            break;

        case "actors":
            filter_data.actors = json_data[value_filter_data];
            break;

        case "directed":
            filter_data.directed = json_data[value_filter_data];
            break;
    }

    filterPerformances(filter_data);
}

$(document).ready(function () {
    $("#rating-filter").change(function () {
        addValueFilter("rating=" + $(this).val());
    });

    $("#age-from-filter").change(function () {
        addValueFilter("age-from=" + $(this).val());
    });

    $("#age-to-filter").change(function () {
        addValueFilter("age-to=" + $(this).val());
    });

    $("#theaters-filter").change(function () {
        addValueFilter("theaters=" + $(this).val());
    });

    $("#genres-filter").change(function () {
        addValueFilter("genres=" + $(this).val());
    });

    $("#actors-filter").change(function () {
        addValueFilter("actors=" + $(this).val());
    });

    $("#directed-filter").change(function () {
        addValueFilter("directed=" + $(this).val());
    });
});