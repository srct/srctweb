from website import db

# project managers
class ProjectManager(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = False)
    username = db.Column(db.String(15), unique = True)
    project = db.Column(db.String(150), unique = False)

    def __repr__(self):
        return '<User %r>' % (self.name)

# developers
class Developer(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = False)
    username = db.Column(db.String(15), unique = True)

    def __repr__(self):
        return '<User %r>' % (self.name)

# contributors
class Contributor(db.model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = False)
    username = db.Column(db.String(15), unique = True)

    def __repr__(self):
        return '<User %r>' % (self.name)

