import os
from flask import Flask, request, g, redirect, url_for, abort, render_template, jsonify
from creditcard import CreditCard

app_creditcard = Flask(__name__)
app_creditcard.config.from_object(__name__)
app_creditcard.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app_creditcard.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app_creditcard.route('/validate', methods=['POST'])
def validate():
  assert request.path == '/validate'
  assert request.method == 'POST'

  print request.form['creditcard']
  cr = CreditCard(request.form['creditcard'])

  if(cr.validate()):
    return jsonify({'creditcard': cr.get_number(), 'valid': True})
  else:
    return jsonify({'creditcard': cr.get_number(), 'valid': False})
