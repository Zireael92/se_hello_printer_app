from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN, XML
from flask import request
import json

moje_imie = "Karolina"
msg = "Hello World!"



@app.route('/')
def index():
    output = request.args.get('output')
    name = request.args.get('name')
    if not output:
        output = PLAIN
    if not name:
        name = moje_imie
    return get_formatted(msg, name,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
