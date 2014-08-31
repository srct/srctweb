from flask import render_template
from website import website

@website.route('/')
def index():
    return render_template("index.html",
        renderHead = False,
    )

@website.route('/calendar/')
def calendar():
    return render_template("calendar.html",
        renderHead = True,
    )

@website.route('/contact/')
def contact():
    return render_template("contact.html",
        renderHead = True,
    )

@website.route('/documents/')
def documents():
    return render_template("documents.html",
        renderHead = True,
    )

@website.route('/people/')
def people():
    return render_template("people.html",
        renderHead = True,
    )

@website.route('/projects/')
def projects():
    return render_template("projects.html",
        renderHead = True,
    )

@website.route('/events/')
def events():
    return render_template("events.html",
        renderHead = True,
    )

@website.route('/opt-out/')
def optOut():
    return render_template("privacy_opt_out.html",

    )

### DOCUMENTS ###

@website.route('/documents/constitution/')
def constitution():
    return render_template("documents/constitution.html",
        renderHead = True,
    )

@website.route('/documents/intellectual_property/')
def intellectualProperty():
    return render_template("documents/intellectual_property.html",
        renderHead = True,
    )

@website.route('/documents/logos/')
def logos():
    return render_template("documents/logos.html",
        renderHead = True,
    )


@website.route('/documents/privacy_policy/')
def privacyPolicy():
    return render_template("documents/privacy_policy.html",
        renderHead = True,
    )

@website.route('/documents/software_freedom/')
def softwareFreedom():
    return render_template("documents/software_freedom.html",
        renderHead = True,
    )

@website.route('/documents/terms_of_service/')
def termsOfService():
    return render_template("documents/terms_of_service.html",
        renderHead = True,
    )

@website.route('/documents/usage_policy/')
def usagePolicy():
    return render_template("documents/usage_policy.html",
        renderHead = True,
    )

# 404 error
@website.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
