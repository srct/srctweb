function checkDate() {
    var d = new Date(),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate()
        year = '' + d.getYear();

    // Mason Pride Week

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

    // Virginia Primaries and General Elections
    // Date reference: https://www.fairfaxcounty.gov/elections/ecalendar

    var primaryMessage = "<div class='alert alert-info mb-0 text-center' role='alert'>" +
                           "<i class='fa fa-info-circle'></i> " +
                           "Today is Virginia's Primary Election. " +
                           "Polls are open from 6:00am - 7:00pm. " +
                           "Photo ID is required. " +
                           "<a href='https://vote.elections.virginia.gov/VoterInformation/'" +
                            "class='alert-link'>" +
                           "Click here to verify your registration status, " +
                           "find your polling place, and review your ballot." +
                           "</a>" +
                         "</div>";

    var generalMessage = primaryMessage.replace(/Primary/i, 'General');

    // primaries are the second Tuesday of June
    if (month == 6) {
        juneFirst = new Date(year, month, 1);
        weekday = juneFirst.getDay();
        // math for date calculation based on information read here
        // http://www.i-programmer.info/programming/javascript/6322-date-hacks-doing-javascript-date-calculations.html
        secondTuesday = 1 + (((2 - weekday) + 7) % 7) + 7;

        if (day == secondTuesday) {
            document.body.insertAdjacentHTML("afterbegin", primaryMessage);
        }

    // generals are the first Tuesday after the first Monday of November
    } else if (month == 11) {
        novemberFirst = new Date(year, month, 1);
        weekday = novemberFirst.getDay();

        // if the first day of the month is a Tuesday
        if (weekday == 1) {
            // the election will be on the 8th
            general = 8;
        } else {
            general = 1 + (((2 - weekday) + 7) % 7);
        }

        if (day == general) {
            document.body.insertAdjacentHTML("afterbegin", generalMessage);
        }
    }
}

window.onload = checkDate
