var datepicker_obj = $("#datepicker");

$(document).ready(function() {
    $.datepicker.regional['ru'] = {
        closeText: 'Закрыть',
        prevText: '&#x3c;Пред',
        nextText: 'След&#x3e;',
        currentText: 'Сегодня',
        monthNames: ['Январь','Февраль','Март','Апрель','Май','Июнь',
        'Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь'],
        monthNamesShort: ['Янв','Фев','Мар','Апр','Май','Июн',
        'Июл','Авг','Сен','Окт','Ноя','Дек'],
        dayNames: ['воскресенье','понедельник','вторник','среда','четверг','пятница','суббота'],
        dayNamesShort: ['вск','пнд','втр','срд','чтв','птн','сбт'],
        dayNamesMin: ['Вс','Пн','Вт','Ср','Чт','Пт','Сб'],
        dateFormat: 'dd.mm.yy',
        firstDay: 1,
        isRTL: false
    };

    $.datepicker.setDefaults($.datepicker.regional['ru']);

    datepicker_obj.datepicker({
        altFormat: "dd.mm.yy",
        showOn: "button",
        buttonImage: "/static/images/datepicker/date.png",
        buttonImageOnly: true,
        buttonText: "Выберите дату",
        minDate: new Date(),
        onSelect: function(dateText, inst) {
            addValueFilter("date="+$(this).val());
        }
    });
});
