# models.py
import flask_sqlalchemy, app, os

# app.app = app modules app variable
app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('db_uri')
db = flask_sqlalchemy.SQLAlchemy(app.app)
print "hi"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)# key
    user_img = db.Column(db.String(250))
    user_name = db.Column(db.String(120))
    text = db.Column(db.String(120))

def __init__ (self,t):
    self.text=t
    
def __repr__ (self): # what's __repr__?
    return '<Message text: %s>' % self.text