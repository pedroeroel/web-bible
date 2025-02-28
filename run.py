from app.app import create_app
from app.config import *

app = create_app()


if __name__ == '__main__':
    if environment == 'development':
        app.run(debug=True)
    else:
        app.run()