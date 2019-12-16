import pytest
from pgbackup import cli


url = "postgres://postgres@posgtres:5432/testdb"


@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser_without_driver(parser):

    with pytest.raises(SystemExit):
        parser.parse_args(["url"])