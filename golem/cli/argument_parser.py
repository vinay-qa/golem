import argparse


def get_parser():
    parser = argparse.ArgumentParser(prog='golem', add_help=False)
    parser.add_argument('-h', '--help', nargs='?', const=True, default=False)
    subparsers = parser.add_subparsers(dest='command')

    # run
    parser_run = subparsers.add_parser('run', add_help=False)
    browser_choices = ['firefox',
                       'chrome',
                       'chrome-remote',
                       'chrome-headless',
                       'chrome-remote-headless',
                       'firefox-remote',
                       'ie',
                       'ie-remote']
    parser_run.add_argument('project', nargs='?', default='')
    parser_run.add_argument('test_or_suite', nargs='?', default='')
    parser_run.add_argument('-b', '--browsers', action='store',
                            nargs='*', default=[],
                            type=str)
    parser_run.add_argument('-t', '--threads', action='store', nargs='?',
                            default=1, type=int)
    parser_run.add_argument('-e', '--environments', action='store',
                            nargs='*', default=[], type=str)
    parser_run.add_argument('-i', '--interactive', action='store_true',
                            default=False)
    parser_run.add_argument('--timestamp', action='store', nargs='?', type=str)
    parser_run.add_argument('-h', '--help', action='store_true')


    # gui
    parser_gui = subparsers.add_parser('gui', add_help=False)

    parser_gui.add_argument('-p', '--port', action='store',
                            nargs='?', default=5000, type=int)
    parser_gui.add_argument('-h', '--help', action='store_true')

    # createproject
    parser_createproject = subparsers.add_parser('createproject',
                                                 add_help=False)
    parser_createproject.add_argument('project')
    parser_createproject.add_argument('-h', '--help', action='store_true')

    # createtest
    parser_createtest = subparsers.add_parser('createtest', add_help=False)
    parser_createtest.add_argument('project')
    parser_createtest.add_argument('test')
    parser_createtest.add_argument('-h', '--help', action='store_true')

    # createsuite
    parser_createsuite = subparsers.add_parser('createsuite', add_help=False)
    parser_createsuite.add_argument('project')
    parser_createsuite.add_argument('suite')
    parser_createsuite.add_argument('-h', '--help', action='store_true')

    # createuser
    parser_createuser = subparsers.add_parser('createuser', add_help=False)
    parser_createuser.add_argument('username')
    parser_createuser.add_argument('password')
    parser_createuser.add_argument('-a', '--admin', action='store_true',
                                   default=False)
    parser_createuser.add_argument('-p', '--projects', nargs='+', default=[])
    parser_createuser.add_argument('-r', '--reports', nargs='+', default=[])
    parser_createuser.add_argument('-h', '--help', action='store_true')

    return parser


def get_admin_parser():
    parser = argparse.ArgumentParser(prog='golem-admin', add_help=False)
    parser.add_argument('-h', '--help', nargs='?', const=True, default=False)
    subparsers = parser.add_subparsers(dest='command')
    
    # createdirectory
    parser_createdirectory = subparsers.add_parser('createdirectory',
                                                   add_help=False)
    parser_createdirectory.add_argument('name')
    parser_createdirectory.add_argument('-h', '--help', action='store_true')
    
    return parser
