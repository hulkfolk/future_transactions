import flask.json
from flask import request, jsonify, send_file
from flask_api import FlaskAPI

from .utils import logger, load_config

# # local run
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

    # http://localhost:5000/v1/report/getFile
    @app.route("/v1/report/getFile/", methods=["GET"])
    def get_price_by_unix(*args, **kwargs):
        logger.info(request.url)
        file_path = f'{DATA_PATH}/output.csv'

        try:
            return send_file(file_path, as_attachment=True)
        except FileNotFoundError:
            error_msg = 'output.csv is not available!'
            logger.exception(error_msg)
            return generate_response(error_msg, 404)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")