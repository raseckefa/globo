from flask import request, jsonify
from flask_restful import Resource 
from sqlalchemy import create_engine 

db_connect = create_engine('sqlite:///base.db')


class Tags(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM tag")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        name = request.json['name'] 

        conn.execute(
            "INSERT INTO tag (name) VALUES ('{}')".format(name))

        query = conn.execute('SELECT * FROM tag ORDER BY id DESC LIMIT 1')
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


class TagsByid(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM tag WHERE id = {}".format(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def put(self, id):
        conn = db_connect.connect()
        name = request.json['name'] 

        conn.execute(
            "UPDATE tag SET name = '{}' WHERE id = {}".format(name, id))

        query = conn.execute("SELECT * FROM tag WHERE id = {}".format(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def delete(self, id):
        conn = db_connect.connect()
        conn.execute("DELETE FROM tag WHERE id = {}".format(id))
        conn.execute("DELETE FROM card_tag WHERE tag_id = {}".format(id))
        return {"status": "success"}
