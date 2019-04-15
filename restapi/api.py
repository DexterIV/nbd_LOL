import flask
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from flask import request, Flask, jsonify
import json

app = Flask(__name__)


##Strona główna
@app.route('/')
def index():
    return '<html><body><h1>Nierelacyjne bazy danych</h1></body></html>'


##Zwraca pierwszych number gier
##wywołanie /league?number=10
@app.route('/league/', methods=['GET'])
def get_league():
    number = request.args.get('number')
    cluster = Cluster()
    session = cluster.connect("league")
    cql = "SELECT * FROM plays LIMIT " + number
    result = session.execute(cql)
    return flask.jsonify(list(result))


##Dodaje grę do ligi
@app.route('/league/', methods=['POST'])
def create_game():
    data = request.data
    data_dict = json.loads(data.decode('utf-8'))
    gameid = data_dict['gameid']
    datablob = data_dict['datablob']
    if gameid is None or datablob is None:
        return "<html><body><h1>Fields cannot be empty!</h1></body></html>"
    else:
        cluster = Cluster()
        session = cluster.connect('league')
        query = "INSERT INTO plays (gameid, datablob) VALUES ( '" + gameid + "','" + datablob + "')";
        session.execute(query)
        return "<html><body><h1>Success</h1></body></html>"


##Zwraca grę podaną w id
@app.route('/league/<gameid>', methods=['GET'])
def get_play(gameid):
    cluster = Cluster()
    session = cluster.connect("league")
    cql = "SELECT * FROM plays WHERE gameid = '" + gameid + "'"
    result = session.execute(cql)
    return flask.jsonify(list(result))


## Usuwa grę z ligi
@app.route('/league/', methods=['DELETE'])
def delete_play():
    data = request.data
    data_dict = json.loads(data.decode('utf-8'))
    gameid = data_dict['gameid']
    cluster = Cluster()
    session = cluster.connect("league")
    if gameid is None:
        return "<html><body><h1>Field cannot be empty!</h1></body></html>"
    else:
        cql = "DELETE FROM plays WHERE gameid = '" + gameid + "'"
        session.execute(cql)
        return 'Success'


## Zmienia dane gry z ligi
@app.route('/league/', methods=['PUT'])
def change_play():
    data = request.data
    data_dict = json.loads(data.decode('utf-8'))
    column_name = data_dict['column_name']
    value = data_dict['value']
    gameid = data_dict['gameid']
    cluster = Cluster()
    session = cluster.connect("league")
    if gameid is None or column_name is None or value is None:
        return "<html><body><h1>Fields cannot be empty!</h1></body></html>"
    else:
        cql = "UPDATE plays SET " + column_name + "='" + value + "' where gameid='" + gameid + "'"
        session.execute(cql)
        return 'Success'


if __name__ == '__main__':
    connection.setup(['127.0.0.1', '172.18.0.2', '172.18.0.3', '172.18.0.4', '172.18.0.5', '172.18.0.6''172.18.0.7',
                      '172.18.0.8''172.18.0.9'], "cqlengine", protocol_version=3)

    app.run(host="0.0.0.0", port=9043, debug=True)
