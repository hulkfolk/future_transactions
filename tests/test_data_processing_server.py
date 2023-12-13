from unittest.mock import patch, Mock

from future_transactions.data_processing_server import process_data


def test_process_data():
    assert process_data() > 0


@patch('os.path.dirname', new=Mock(return_value='/opt'))
def test_process_data_file_not_found():
    assert process_data() is None


@patch('pandas.read_fwf', new=Mock(return_value=None))
def test_process_data_pandas_error():
    assert process_data() is None
