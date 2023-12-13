from unittest.mock import patch, Mock

from future_transactions.utils import load_config


def test_load_config():
    assert load_config() == {'data_path': '/opt/data/future_transactions'}


@patch('os.path.dirname', new=Mock(return_value='/opt'))
def test_load_config_exception():
    assert load_config() == {}
