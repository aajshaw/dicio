from flask import render_template, Response
from app import app
from app.models import Switches
import subprocess

# Change this command to whatever activates a switch
command = '/home/pi/rfoutlet'

@app.route('/')
@app.route('/index')
def index():
  switches = Switches.query.order_by(Switches.id)
  return render_template('index.html', title = 'Remote switches', switches = switches)

@app.route('/switches')
def switches():
  switches = Switches.query.order_by(Switches.id)
  return render_template('switches.html', title = 'Remote switches', switches = switches)

@app.route('/on/<int:id>', methods = ['POST'])
def on(id):
  switch = Switches.query.get(id)
  print('Turn {} switch ON'.format(switch.description))
  switchIt(switch.switch_id, 'on')
  return Response('Done', status = 200)

@app.route('/off/<int:id>', methods = ['POST'])
def off(id):
  switch = Switches.query.get(id)
  print('Turn {} switch OFF'.format(switch.description))
  switchIt(switch.switch_id, 'off')
  return Response('Done', status = 200)

@app.route('/all-on', methods = ['POST'])
def all_on():
  switches = Switches.query.order_by(Switches.id)
  for switch in switches:
    print('Turn {} switch ON'.format(switch.description))
    switchIt(switch.switch_id, 'on')
  return Response('Done', status = 200)

@app.route('/all-off', methods = ['POST'])
def all_off():
  switches = Switches.query.order_by(Switches.id)
  for switch in switches:
    print('Turn {} switch OFF'.format(switch.description))
    switchIt(switch.switch_id, 'off')
  return Response('Done', status = 200)

def switchIt(id, toggle):
  status = subprocess.run([command, id, toggle])
  print('Status for {} on switch {}: {}'.format(toggle, id, status))
  if status.returncode != 0:
    print('Return code: ' + status.returncode)
