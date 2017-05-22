import config
from mock import mock_open, patch


def test_valid_config_file():
    fake_yml_config = """fake-graph-facebook-server:
  port: <PORT>

web-hook:
  url: <URL>
  port: <PORT>
    """

    with patch("builtins.open", mock_open(read_data=fake_yml_config)):
        config_dict = config.config()
        assert config_dict.get("fake-graph-facebook-server")
        assert config_dict.get("web-hook")
