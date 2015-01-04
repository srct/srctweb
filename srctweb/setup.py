import sys

# python 3
input = raw_input

if __name__ == '__main__':
    from website import db
    db.create_all()

    from website.models import Member
    name = input("Please enter your name: ")
    username = input("Please enter your gmu-username: ")
    dev = Member(name=name, username=username, developer=True)
    db.session.add(dev)
    db.session.commit()
