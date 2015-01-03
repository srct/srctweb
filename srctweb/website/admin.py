from website import srctweb, db
from website.models import Member, Executive, Project, Meeting 
from flask import request, render_template, redirect
# flask-login
from flask.ext.login import LoginManager, login_user, current_user
login_manager = LoginManager()
login_manager.init_app(srctweb)


@login_manager.user_loader
def load_user(userid):
    return Member.query.get(userid)

from flask_ldap_login import LDAPLoginForm, LDAPLoginManager
import ldap
LDAP = {
    'URI': 'ldaps://directory.gmu.edu:636',
    'BIND_DN': 'uid=%(username)s,ou=people,o=gmu.edu',
    'BIND_AUTH': 'uid=%(username)s,ou=people,o=gmu.edu',
    'KEY_MAP': {
        "first_name": "givenName",
        "last_name": "sn",
        "email": "mail"
    },
    'OPTIONS': {
        ldap.OPT_X_TLS: ldap.OPT_X_TLS_DEMAND,
        ldap.OPT_X_TLS_REQUIRE_CERT: ldap.OPT_X_TLS_NEVER,
    }

}  # LDAP Settings
srctweb.config.update(LDAP=LDAP)
ldap_manager = LDAPLoginManager(srctweb)


@srctweb.route('/admin/login', methods=['GET', 'POST'])
def ldap_login():
    if request.method == "GET":
        return render_template('login.html')
    
    if not ('username' in request.form and 'password' in request.form):
        return render_template('login.html')

    username = request.form['username']
    password = request.form['password']
    user_dict = ldap_manager.ldap_login(username, password)

    if not user_dict:
        return render_template('login.html')
    
    user = Member.query.filter(Member.username == username).first()
    # make a new Member!
    if not user:
        user = Member(name=user_dict['first_name'] + ' ' + user_dict['last_name'],
                       username=username,
                       developer=False)
        db.session.add(user)
        db.session.commit()
    login_user(user, remember=True)
    return redirect('/admin')


# flask-admin
from flask.ext.admin import Admin as FlaskAdmin
from flask.ext.admin.contrib.sqla import ModelView
admin = FlaskAdmin(srctweb)

class SRCTModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated() and current_user.developer

admin.add_view(SRCTModelView(Member, db.session))
admin.add_view(SRCTModelView(Executive, db.session))
admin.add_view(SRCTModelView(Project, db.session))
admin.add_view(SRCTModelView(Meeting, db.session))

