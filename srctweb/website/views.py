from flask import render_template
from website import website

@website.route('/')
@website.route('/index')
def index():
    return render_template("index.html",
    
    )

@website.route('/calendar')
def calendar():
    return render_template("calendar.html",
    
    )

@website.route('/contact')
def contact():
    return render_template("contact.html",
    
    )

@website.route('/documents')
def documents():
    return render_template("documents.html",
    
    )


@website.route('/events')
def events():
    return render_template("events.html",
    
    )

@website.route('/meetings')
def meetings():
    return render_template("meetings.html",
    
    )

@website.route('/people')
def people():
    return render_template("people.html",
    
    )

@website.route('/projects')
def projects():
    return render_template("projects.html",

    )

### DOCUMENTS ###

@website.route('/constitution')
def constitution():
    return render_template("documents/constitution.html",
    
    )

@website.route('/intellectual_property')
def intellectualProperty():
    return render_template("documents/intellectual_property.html",
    
    )

@website.route('/logos')
def logos():
    return render_template("documents/logos.html",
    
    )


@website.route('/privacy_policy')
def privacyPolicy():
    return render_template("documents/privacy_policy.html",
    
    )

@website.route('/software_freedom')
def softwareFreedom():
    return render_template("documents/software_freedom.html",
    
    )

@website.route('/terms_of_service')
def termsOfService():
    return render_template("documents/terms_of_service.html",
    
    )

@website.route('/usage_policy')
def usagePolicy():
    return render_template("documents/usage_policy.html",

    )
