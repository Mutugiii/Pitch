from app import create_app
from flask_script import Manager, Server

app = create_app('development')
test_app = create_app('test')

manager = Manager(app)
manager.add_command('serve',Server)
if __name__ == '__main__':
    manager.run()
