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

if __name__ == '__main__':
    globals()[sys.argv[1]]()