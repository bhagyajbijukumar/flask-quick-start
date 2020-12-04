from main import create_app

app = create_app(config_file="config.cfg")

app.run()