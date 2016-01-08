"""
Class : Main
Description: Entry point for console
"""
import logging
import sys
import os
import argparse

from cliff.app import App
from cliff.commandmanager import CommandManager

class RedditCli(App):
    log = logging.getLogger(__name__)

    def __init__(self):
        super(RedditCli, self).__init__(
            description='Reddit Cli',
            version='0.1',
            command_manager=CommandManager('reddit.cli')
        )

    def initialize_app(self, argv):
        self.log.debug('Initializing redditcli app')

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('Error occurred : %s', err)
    
    def configure_logging(self):
        log_lvl = logging.DEBUG if self.options.debug else logging.WARNING
        logging.basicConfig(
            format="%(levelname)s (%(module)s) %(message)s",
            level=log_lvl)
        logging.getLogger('iso8601').setLevel(logging.WARNING)
        if self.options.verbose_level <= 1:
            logging.getLogger('requests').setLevel(logging.WARNING)

    def build_option_parser(self, description, version, argparse_kwargs=None):
        argparse_kwargs = argparse_kwargs or {}
        parser = argparse.ArgumentParser(
            description=description,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            **argparse_kwargs
        )
        parser.add_argument(
            '--version',
            action='version',
            version='%(prog)s {0}'.format(version),
            help='Show program\'s version number and exit',
        )

        parser.add_argument(
            '--debug',
            default=False,
            action='store_true',
            help='Show program\'s version number and exit',
        )

        # parser.add_argument(
        #     '-v', '--verbose',
        #     action='count',
        #     dest='verbose_level',
        #     default=logging.DEBUG,
        #     help='Increase verbosity of output. Can be repeated.',
        # )

        parser.add_argument(
            '--redditapi-url',
            action='store',
            dest='redditapi_url',
            default='https://oauth.reddit.com',
            help='Reddit API url',
        )

        parser.add_argument(
            '--client-id',
            action='store',
            dest='client_id',
            default=os.environ.get('REDDIT_CLIENT_ID'),
            help='Client ID for your registered application.',
        )

        parser.add_argument(
            '--client-secret',
            action='store',
            dest='client_secret',
            default=os.environ.get('REDDIT_CLIENT_SECRET'),
            help='Secret token for your registered Client application',
        )

        parser.add_argument(
            '--username',
            action='store',
            dest='username',
            default=os.environ.get('REDDIT_USERNAME'),
            help='Username for your registered Client application',
        )

        parser.add_argument(
            '--password',
            action='store',
            dest='password',
            default=os.environ.get('REDDIT_PASSWORD'),
            help='Password for your registered Client application',
        )

        parser.add_argument(
            '--user_agent',
            action='store',
            dest='user_agent',
            default='python-app/0.1 by RedditCli',
            help='User agent name for your registered Client application',
        )

        return parser

def main(argv=sys.argv[1:]):
    app = RedditCli()
    return app.run(argv)