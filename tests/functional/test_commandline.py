import pytest
from redditcli.main import RedditCli

@pytest.fixture(scope='module')
def app():
    cli = RedditCli()
    return cli

def test_without_args(app):
    argv = []
    app.run(argv)

def test_with_args(app):
    argv = ['-123131312','aefdsfasf','asdfdsaf']
    app.run(argv)
