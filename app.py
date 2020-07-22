from back.models import create_app
from back.config import config

enviroment = config['production']
app = create_app(enviroment)

if __name__ == "__main__":
    app.run()
