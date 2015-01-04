from website import srctweb
from website import db


# Dynamic reference table of Developers and their associated projects.
developers = db.Table('developers',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
    db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
    db.Column('role', db.String(150))
)


# Dynamic reference table of Event staff.
event_staff = db.Table('event_staff',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id')),
    db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
    db.Column('role', db.String(150))
)


# Executive membership.
class Executive(db.Model):
    __tablename__ = "executives"

    # Map executives directly onto members.
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), primary_key=True)
    member = db.relationship('Member')
    title = db.Column(db.String(150), unique=True)

    # Initialization function.
    def __init__(self, username, title):
        member = Member.query.filter_by(username=username).first()
        self.member_id = member.id
        self.member = member
        self.title = title

    # Textual representation.
    def __repr__(self):
        username = self.member.username
        return '<%r: %r>' % (self.title, username)


# Standard SRCT member (developer or contributor).
class Member(db.Model):

    # Human metadata.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False)
    username = db.Column(db.String(15), unique=True)
    active = db.Column(db.Boolean, default=True)

    # Developer status.
    developer = db.Column(db.Boolean, unique=False)

    # Associated projects using reference table (secondary).
    projects = db.relationship('Project',
            secondary=developers,
            backref=db.backref('developers'))

    # Projects this member manages.
    manages = db.relationship('Project',
            backref='manager',
            lazy='dynamic')

    # Associated events using reference table (secondary).
    events = db.relationship('Event',
            secondary=event_staff,
            backref=db.backref('staff'))

    # Events this member is POC for.
    pocs = db.relationship('Event',
            backref='point_of_contact',
            lazy='dynamic')

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False  # no Anons in here

    def is_authenticated(self):
        """All users are authed through ldap so return true"""
        return True

    def get_id(self):
        return self.id

    # Textual representation.
    def __repr__(self):
        dev_status = "Developer" if self.developer else "Contributor"
        return '<%r: %r>' % (dev_status, self.username)

    # let flask-admin handle this
    # # Initialization function.
    # def __init__(self, name, username):
    #     self.name = name
    #     self.username = username
    #     self.developer = False


# Standard SRCT project with a name and project manager.
class Project(db.Model):

    # Project metadata.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False)

    url = db.Column(db.String(150), unique=False)
    repo = db.Column(db.String(150), unique=False)
    desc = db.Column(db.String(500), unique=False)

    # ID of the project manager.
    manager_id = db.Column(db.Integer,
            db.ForeignKey('member.id'),
            unique=False)

    # Textual representation.
    def __repr__(self):
        return '<Project: %r>' % (self.name)

    # let flask-admin handle
    # # Initialization function.
    # def __init__(self, name):
    #     self.name = name


# SRCT affiliated events.
class Event(db.Model):

    # Event metadata.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False)
    abbrev = db.Column(db.String(20), unique=True)
    page = db.Column(db.String(20), unique=False)

    # ID of the event point of contact.
    point_of_contact_id = db.Column(db.Integer,
            db.ForeignKey('member.id'),
            unique=False)

    # Textual representation.
    def __repr__(self):
        return '<Event: %r>' % (self.name)

    # let flask-admin handle
    # # Initialization function.
    # def __init__(self, name, abbrev=None, page=None):
    #     self.name = name
    #     if abbrev is None:
    #         abbrev = name
    #     self.abbrev = abbrev
    #     if page is None:
    #         page = abbrev + ".html"
    #     self.page = page


# Meeting dates.
class Meeting(db.Model):

    # Meeting metadata.
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, unique=False)
    location = db.Column(db.String(150), unique=False)

    # Textual representation.
    def __repr__(self):
        return '<Meeting: (%r) (%r)>' % (self.date_time.strftime("%B %d %r"),
                                            self.location)

    # let flask-admin handle
    # # Initialization function.
    # def __init__(self, location, year, month, day, hour, minute=0):

    #     # Construct datetime object.
    #     from datetime import datetime
    #     date_time = datetime(year,month,day,hour,minute)

    #     self.date_time = date_time
    #     self.location = location

