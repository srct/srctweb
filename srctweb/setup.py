import sys

if __name__ == '__main__':
    from website import db
    db.create_all()

    from website.models import Member
    dev = Member(name=sys.argv[1], username=sys.argv[2], developer=True)
    db.session.add(dev)
    db.session.commit()
