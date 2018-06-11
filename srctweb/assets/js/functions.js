function checkDate() {
    var d = new Date(),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate()
        year = '' + d.getYear();
    // if it is March
    if (month == 3) {
        // find out what the third week of March is
        var marchFirst = new Date(year, month, 1);
        // days of the week are 0 - 6
        // Sunday is 0
        var weekday = marchFirst.getDay();
        var daysInFirstWeek = 7 - weekday;
        // hopefully they won't schedule a different week
        // overlap from March into April would be especially annoying
        var thirdWeek = daysInFirstWeek + 14;
        var fourthWeek = daysInFirstWeek + 21;

        if (day > thirdWeek && day <= fourthWeek){
            // appends the pride bar to existing classes,
            // maintaining all of the Masonstrap formatting
            document.body.className += " pride-bar";
        }
    }
}
window.onload = checkDate
