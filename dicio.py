from app import app, db
from app.models import Switches

@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'Switches': Switches}

  if __name__ == '__main__':
    app.run(host='0.0.0.0')
