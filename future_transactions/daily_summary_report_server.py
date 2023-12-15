import pandas as pd
import flask.json
from flask import request, jsonify, send_file, render_template
from flask_api import FlaskAPI


from .utils import logger, load_config

# # local test
# from future_transactions.utils import logger, load_config


DATA_PATH = load_config().get('data_path', '/opt/data/future_transactions')


def generate_response(results, status_code):
    response = jsonify(results)
    response.data = flask.json.dumps(results).encode()
    response.status_code = status_code
    logger.info(response.status_code)
    return response


def create_app():
    app = FlaskAPI(__name__, instance_relative_config=True)

    @app.route("/")
    def index_page():
        return render_template('index.html')

    # http://localhost:5000/v1/report/getFile
    @app.route("/v1/report/getFile/", methods=["GET"])
    def get_file(*args, **kwargs):
        logger.info(request.url)
        file_path = f'{DATA_PATH}/output.csv'

        try:
            return send_file(file_path, as_attachment=True)
        except FileNotFoundError:
            error_msg = 'output.csv is not available!'
            logger.exception(error_msg)
            return generate_response(error_msg, 404)

    # http://localhost:5000/v1/report/getData
    @app.route("/v1/report/getData/", methods=["GET"])
    def get_data(*args, **kwargs):
        logger.info(request.url)
        file_path = f'{DATA_PATH}/output.csv'
        try:
            df = pd.read_csv(file_path)[['Client_Information', 'Product_Information', 'Total_Transaction_Amount']]
            items = df.to_dict('records')
            status_code = 200
        except:
            logger.exception('Failed to load transactions data!')
            items, status_code = [], 500
        return generate_response({'items': items}, status_code)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")