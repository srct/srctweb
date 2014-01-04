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
