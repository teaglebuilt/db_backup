from argparse import ArgumentParser, Action

drivers = ['local', 'docker']


class DriverAction(Action):
    pass


def create_parser():
    parser = ArgumentParser()
    parser.add_argument('url', help="URL of postgres db")
    parser.add_argument('--driver', '-d', 
        help='backup storage direction',
        nargs=2,
        action=DriverAction,
        metavar=('driver', 'destination'),
        required=True
    )
    return parser


def main():
    import time
    import boto3

    args = create_parser().parse_args()
    