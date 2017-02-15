# models.py
import flask_sqlalchemy, app

# app.app = app modules app variable
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bavery:Logic891@localhost/postgres'
db = flask_sqlalchemy.SQLAlchemy(app.app)
print "hi"

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)# key
    text = db.Column(db.String(120))

def __init__ (self,t):
    self.text=t
    
def __repr__ (self): # what's __repr__?
    return '<Message text: %s>' % self.text