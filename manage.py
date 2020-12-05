import sys

def create_all():
    from main import create_app
    app = create_app(config_file="config.cfg")
    from extensions import db
    db.create_all(app=app)

def runserver():
    from main import create_app
    app = create_app(config_file="config.cfg")
    app.run(debug=True)


def createsuperuser():
    from helpers import userhelpers
    import getpass
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = getpass.getpass("Enter password: ")
    userhelpers.create_user(username=username,email=email,password=password,verified=True)

if __name__ == '__main__':
    globals()[sys.argv[1]]()