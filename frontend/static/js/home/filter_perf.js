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
            if(json_data[value_filter_data] == 0) {
                delete filter_data.rating
            } else {
                filter_data.rating = json_data[value_filter_data];
            }
            break;

        case "age-from":
            if(json_data[value_filter_data] == 0) {
                delete filter_data.age_from
            } else {
                filter_data.age_from = json_data[value_filter_data];
            }
            break;

        case "age-to":
            if(json_data[value_filter_data] == 0) {
                delete filter_data.age_to
            } else {
                filter_data.age_to = json_data[value_filter_data];
            }
            break;

        case "theaters":
            if(json_data[value_filter_data] == 0) {
                delete filter_data.theaters
            } else {
                filter_data.theaters = json_data[value_filter_data];
            }
            break;

        case "genres":
            if(json_data[value_filter_data] == 0) {
                delete filter_data.genres
            } else {
                filter_data.genres = json_data[value_filter_data];
            }
            break;

        case "actors":
            if(json_data[value_filter_data] == 0) {
                delete filter_data.actors
            } else {
                filter_data.actors = json_data[value_filter_data];
            }
            break;

        case "directed":
            if(json_data[value_filter_data] == 0) {
                delete filter_data.directors
            } else {
                filter_data.directors = json_data[value_filter_data];
            }
            break;
    }

    filterPerformances(filter_data);
}


function clear_filter() {
    $("#filter-form").submit(function(e){
        e.preventDefault();
        $('.bts-select').val(0);
        $('.bts-select').selectpicker('refresh');
        $(datepicker_obj).datepicker('setDate', null);
        filter_data = {};
        filterPerformances(filter_data);
    });
}

$(document).ready(function () {
    clear_filter();

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