from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return "Hello World Babaca!"

@app.route('/api/v1/hello_name', methods=['POST'])
def hello_with_name():
    data = request.get_json()
    try:
        if str(data).strip() <> '{}':
            return jsonify('Hello World {}'.format(data.get('name')))
        else:
            retorno = {'message': 'Necessário informar o parâmetro name'}
            return jsonify(retorno), 204
    except RuntimeError:
        return jsonify('Ocorreu um erro'), 500

@app.route('/api/v1/tabuada', methods=['GET'])
def get_tabuada():
    data = request.get_json()
    try:
        result = ''
        for i in range(1, 10):
           result += '{} X {} = {} '.format(data.get('num'), i, data.get('num') * i)
        return jsonify(result)
    except RuntimeError as ex:
        return jsonify('Ocorreu um erro ao calcular a tabuada do {} -  Exception: {}'.format(data.get('num'), ex))        

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)        