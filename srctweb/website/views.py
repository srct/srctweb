from flask import render_template
from website import srctweb
from website.models import Meeting


@srctweb.route('/')
def index():

    # Access most recent meeting.
    next_meeting = Meeting.query.order_by("date_time")[0]

    date = next_meeting.date_time.strftime("%B %d")
    time = next_meeting.date_time.strftime("%r")
    location = next_meeting.location

    return render_template("index.html",
        renderHead = False,
        next_meeting_date = date,
        next_meeting_time = time,
        next_meeting_location = location,
    )

@srctweb.route('/calendar/')
def calendar():
    return render_template("calendar.html",
        renderHead = True,
    )

@srctweb.route('/contact/')
def contact():
    return render_template("contact.html",
        renderHead = True,
    )

@srctweb.route('/documents/')
def documents():
    return render_template("documents.html",
        renderHead = True,
    )

@srctweb.route('/people/')
def people():
    return render_template("people.html",
        renderHead = True,
    )

@srctweb.route('/projects/')
def projects():
    return render_template("projects.html",
        renderHead = True,
    )

@srctweb.route('/events/')
def events():
    return render_template("events.html",
        renderHead = True,
    )

@srctweb.route('/opt-out/')
def optOut():
    return render_template("privacy_opt_out.html",

    )

### DOCUMENTS ###

@srctweb.route('/documents/constitution/')
def constitution():
    return render_template("documents/constitution.html",
        renderHead = True,
    )

@srctweb.route('/documents/intellectual_property/')
def intellectualProperty():
    return render_template("documents/intellectual_property.html",
        renderHead = True,
    )

@srctweb.route('/documents/logos/')
def logos():
    return render_template("documents/logos.html",
        renderHead = True,
    )


@srctweb.route('/documents/privacy_policy/')
def privacyPolicy():
    return render_template("documents/privacy_policy.html",
        renderHead = True,
    )

@srctweb.route('/documents/software_freedom/')
def softwareFreedom():
    return render_template("documents/software_freedom.html",
        renderHead = True,
    )

@srctweb.route('/documents/terms_of_service/')
def termsOfService():
    return render_template("documents/terms_of_service.html",
        renderHead = True,
    )

@srctweb.route('/documents/usage_policy/')
def usagePolicy():
    return render_template("documents/usage_policy.html",
        renderHead = True,
    )

# 404 error
@srctweb.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
