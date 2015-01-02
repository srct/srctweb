from website import srctweb, db
from website import models
from flask import request, render_template, redirect
# flask-login
from flask.ext.login import LoginManager, login_user
login_manager = LoginManager()
login_manager.init_app(srctweb)


from flask_ldap_login import LDAPLoginForm, LDAPLoginManager
import ldap
LDAP = {
    'URI': 'ldaps://directory.gmu.edu:636',
    'BIND_DN': 'ou=people,o=gmu.edu',
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
    form = LDAPLoginForm(request.form)
    import pdb; pdb.set_trace();
    if form.validate_on_submit():
        login_user(form.user, remember=True)
        print "Valid"
        return redirect('/admin')
    else:
        print "Invalid"
    return render_template('login.html', form=form)


# flask-admin
from flask.ext.admin import Admin as FlaskAdmin
from flask.ext.admin.contrib.sqla import ModelView
admin = FlaskAdmin(srctweb)

class SRCTModelView(ModelView):
    def is_accessible(self):
        return

admin.add_view(ModelView(models.Member, db.session))
admin.add_view(ModelView(models.Executive, db.session))
admin.add_view(ModelView(models.Project, db.session))
admin.add_view(ModelView(models.Meeting, db.session))
