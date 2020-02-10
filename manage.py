from app import create_app
from flask_script import Manager, Server
from app.models import User,Role

app = create_app('development')
test_app = create_app('test')

manager = Manager(app)
manager.add_command('serve',Server)

# create a shel context
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role)
if __name__ == '__main__':
    manager.run()
