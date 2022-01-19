import csv
from sqlalchemy import create_engine

db_connect = create_engine('sqlite:///base.db')
conn = db_connect.connect()

fileName = input('Informe o caminho e nome do arquivo .csv para importação: ')
with open(fileName) as csv_file:
    lines = csv.reader(csv_file, delimiter=',')
    for line in lines:
        try:
            texto = line[0].strip()
            tags = line[1].strip()
            sql = "INSERT INTO card (texto, data_criacao) VALUES ('{}', CURRENT_TIMESTAMP)".format(
                texto)
            conn.execute(sql)

            query = conn.execute('SELECT * FROM card ORDER BY id DESC LIMIT 1')
            result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]

            if tags != '':
                tagArr = tags.split(';')
                for tag in tagArr:
                    try:
                        tag = tag.strip()
                        if tag == '':
                            continue

                        sql = "INSERT OR IGNORE INTO tag (name) VALUES ('{}')".format(
                            tag, tag) 
                        conn.execute(sql)
                        sql = "INSERT INTO card_tag (card_id, tag_id) VALUES ({}, (SELECT id FROM tag WHERE name = '{}'))".format(
                            result[0]["id"], tag) 
                        conn.execute(sql)

                        print(f'SALVA TAG {tag}')
                    except:
                        print(f'ERRO TAG {tag}')

            print(f'SALVO CARD {texto}')
        except:
            print(f'ERRO CARD {texto}')

print(f'FIM DO PROCESSAMENTO')
