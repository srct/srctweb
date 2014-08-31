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


# Standard SRCT member (developer or contributor).
class Member(db.model):

    # Human metadata.
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = False)
    username = db.Column(db.String(15), unique = True)

    # Developer status.
    developer = db.Column(db.Boolean, unique = False)

    # Associated projects using reference table (secondary).
    projects = db.relationship('Project',
            secondary = developers,
            backref = db.backref('developers'))

    # Associated events using reference table (secondary).
    events = db.relationship('Event',
            secondary = event_staff,
            backref = db.backref('staff'))

    # Textual representation.
    def __repr__(self):
        return '<%r>' % (self.username)


# Standard SRCT project with a name and project manager.
class Project(db.model):

    # Project metadata.
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = False)

    # ID of the project manager.
    manager_id = db.Column(db.Integer,
            db.ForeignKey('member.id'),
            unique = False)

    # Textual representation.
    def __repr__(self):
        return '<%r>' % (self.name)


# SRCT affiliated events.
class Event(db.model):

    # Event metadata.
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = False)

    # ID of the event point of contact.
    point_of_contact_id = db.Column(db.Integer,
            db.ForeignKey('member.id'),
            unique = False)
