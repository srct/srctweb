from flask import render_template
from website import website

@website.route('/')
@website.route('/index')
def index():
    return render_template("index.html",
    
    )

def calendar():
    return render_template("calendar.html",
    
    )

def contact():
    return render_template("contact.html",
    
    )

def documents():
    return render_template("documents.html",
    
    )

def meetings():
    return render_template("meetings.html",
    
    )

def people():
    return render_template("people.html",
    
    )

def projects():
    return render_template("projects.html",

    )
