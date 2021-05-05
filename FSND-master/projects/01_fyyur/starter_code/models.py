from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(500))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref='venue', passive_deletes=True)

    def __repr__(self):
      return '<Venue ' + str(self.id) + ' '+ str(self.name)+ '>'
      @property
      def search(self):
        return{
          'id' :self.id,
          'name' :self.name
        }

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500))
    seeking_venue =db.Column(db.String(500))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref='artist', passive_deletes=True)

    def __repr__(self):
      return '<Artist ' + str(self.id) + ' '+ str(self.name)+ '>'


# TODO: implement any missing fields, as a database migration using Flask-Migrate
# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
    __tablename__='Show'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, default=datetime.utcnow())
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id', ondelete='CASCADE'))
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id', ondelete='CASCADE'))

    def __repr__(self):
      return '<Show ' + str(self.id) + ' '+ str(self.start_time)+ '>'

  

  