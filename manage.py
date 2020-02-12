from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User,Pitch

app = create_app('development')
# test_app = create_app('test')

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('serve',Server)
manager.add_command('db', MigrateCommand)

# Run app tests
@manager.command
def test():
    """Running unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# create a shell context
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Pitch = Pitch)


if __name__ == '__main__':
    manager.run()
