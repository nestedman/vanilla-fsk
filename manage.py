from flask_script import Manager
from app import app

manage = Manager(app)

if __name__ == '__main__':
    manager.run()