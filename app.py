from main import create_app

app = create_app(config_file="config.cfg")

if __name__ == "__main__":
    app.run()