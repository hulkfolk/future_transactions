from unittest.mock import patch, Mock

from flask import Response


@patch('future_transactions.daily_summary_report_server.send_file',
       Mock(return_value=Response(status='200 OK', headers=[('Content-Disposition', 'attachment; filename=output.csv')])))
def test_get_file(client):
    response = client.get('/v1/report/getFile/')
    assert response.status_code == 200
    assert response.headers['Content-Disposition'] == 'attachment; filename=output.csv'


@patch('future_transactions.daily_summary_report_server.DATA_PATH', new=Mock(return_value=''))
def test_get_file_exception(client):
    response = client.get('/v1/report/getFile/')
    assert response.status_code == 404
    assert response.data == b'"output.csv is not available!"'

