from flask import Flask, request, Response, jsonify;
from flask_restful import Resource, Api, reqparse;
from flask.ext.mysql import MySQL;
import json;

app = Flask(__name__);

#MySQL configurations
app.config['MYSQL_DATABASE_USER']       ='root';
app.config['MYSQL_DATABASE_PASSWORD']   ='root1234';
app.config['MYSQL_DATABASE_DB']         ='analysis_app_db';
app.config['MYSQL_DATABASE_HOST']       ='localhost';

mysql=MySQL();
mysql.init_app(app);


class Tag(Resource):
    def get(self):
        try:
            query_result = execute_query("SELECT * FROM tb_tag");
            data = json.dumps(query_result);
            resp = Response(data, status=200, mimetype='application/json');
            return resp;

        except Exception as e:
            return {'error':str(e)};


class Test(Resource):
    def get(self):
        try:
            jsonParams = request.get_json();
            jjson = json.loads(jsonParams);

            queryStr = "select * from tb_tag";

            for key in jjson:
                print(jjson[key]);

            return 'ok';
        except Exception as e:
            return {'error':str(e)};


def execute_query(query, one=False):
    cursor = mysql.connect().cursor();
    cursor.execute(query)
    rv = [dict((cursor.description[idx][0], value)
    for idx, value in enumerate(row)) for row in cursor.fetchall()]
    return (rv[0] if rv else None) if one else rv;
