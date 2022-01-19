from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///base.db')


class Cards(Resource):
    def get(self): 
        conn = db_connect.connect()
        query = conn.execute("""SELECT c.*, group_concat(t.name) AS tag 
            FROM card c 
                LEFT JOIN card_tag ct ON ct.card_id = c.id 
                LEFT JOIN tag t ON ct.tag_id = t.id
            GROUP BY c.id, c.texto, c.data_criacao, c.data_modificacao
            ORDER BY c.data_modificacao DESC, c.data_criacao DESC""")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        texto = request.json['texto']

        sql = "INSERT INTO card (texto, data_criacao) VALUES ('{}', CURRENT_TIMESTAMP)".format(
            texto)
        conn.execute(sql)

        sql = "SELECT * FROM card ORDER BY id DESC LIMIT 1"
        query = conn.execute(sql)
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]

        if 'tags' in request.json:
            tags = request.json['tags']
            tagArr = tags.split(',')
            for tag in tagArr:
                tag = tag.strip()
                if tag == '':
                    continue

                sql = "INSERT OR IGNORE INTO tag (name) VALUES ('{}')".format(
                    tag, tag)
                conn.execute(sql)
                sql = "INSERT INTO card_tag (card_id, tag_id) VALUES ({}, (SELECT id FROM tag WHERE name = '{}'))".format(
                    result[0]["id"], tag)
                conn.execute(sql)

        return jsonify(result)


class CardsByid(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("""SELECT c.*, group_concat(t.name) AS tag 
            FROM card c 
                LEFT JOIN card_tag ct ON ct.card_id = c.id 
                LEFT JOIN tag t ON ct.tag_id = t.id
            WHERE c.id = {}
            GROUP BY c.id, c.texto, c.data_criacao, c.data_modificacao""".format(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def put(self, id):
        conn = db_connect.connect()
        texto = request.json['texto']

        sql = "UPDATE card SET texto = '{}', data_modificacao = CURRENT_TIMESTAMP WHERE id = {}".format(
            texto, id)
        conn.execute(sql)
        sql = "DELETE FROM card_tag WHERE card_id = {}".format(id)
        conn.execute(sql)

        if 'tags' in request.json:
            tags = request.json['tags']
            tagArr = tags.split(',')
            for tag in tagArr:
                tag = tag.strip()
                if tag == '':
                    continue

                sql = "INSERT OR IGNORE INTO tag (name) VALUES ('{}')".format(
                    tag, tag)
                conn.execute(sql)
                sql = "INSERT INTO card_tag (card_id, tag_id) VALUES ({}, (SELECT id FROM tag WHERE name = '{}'))".format(
                    id, tag)
                conn.execute(sql)

        query = conn.execute("SELECT * FROM card WHERE id = {}".format(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def delete(self, id):
        conn = db_connect.connect()
        conn.execute("DELETE FROM card WHERE id = {}".format(id))
        conn.execute("DELETE FROM card_tag WHERE card_id = {}".format(id))
        return {"status": "success"}


class CardsBytag(Resource):
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("""SELECT c.*, group_concat(t.name) AS tag 
            FROM card c 
                LEFT JOIN card_tag ct ON ct.card_id = c.id 
                LEFT JOIN tag t ON ct.tag_id = t.id
            WHERE t.id IN ({})
            GROUP BY c.id, c.texto, c.data_criacao, c.data_modificacao""".format(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)
        

class CardsByAny(Resource):
    def get(self, texto):
        conn = db_connect.connect()
        query = conn.execute("""SELECT c.*, group_concat(t.name) AS tag 
            FROM card c 
                LEFT JOIN card_tag ct ON ct.card_id = c.id 
                LEFT JOIN tag t ON ct.tag_id = t.id
            WHERE upper(c.texto) LIKE upper('%{}%') OR upper(t.name) LIKE upper('%{}%')
            GROUP BY c.id, c.texto, c.data_criacao, c.data_modificacao""".format(texto, texto))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)
