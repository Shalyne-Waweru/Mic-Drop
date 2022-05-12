from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pickup,PickupComments,PickupLikes,PickupDislikes,Interview,InterviewComments,InterviewLikes,InterviewDislikes,Promotion,PromotionComments,PromotionLikes,PromotionDislikes
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Pickup = Pickup, PickupComments = PickupComments, PickupLikes = PickupLikes, PickupDislikes = PickupDislikes, Interview = Interview, InterviewComments = InterviewComments, Promotion = Promotion, InterviewLikes = InterviewLikes, InterviewDislikes = InterviewDislikes, PromotionComments = PromotionComments, PromotionLikes = PromotionLikes, PromotionDislikes = PromotionDislikes)

if __name__ == '__main__':
    manager.run()