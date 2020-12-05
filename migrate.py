from main import create_app
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models import *


app = create_app(config_file="config.cfg")
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()