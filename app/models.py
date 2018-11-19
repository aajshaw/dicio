from app import db

class Switches(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  description = db.Column(db.String(128), index = True, unique = True)
  switch_id = db.Column(db.String(32))

  def __repr__(self):
    return '<Switch: {}>'.format(self.description)
