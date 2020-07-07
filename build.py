#!/usr/bin/env python
import os
import sys


def usage():
    print('Run manage tasks.')
    print('Usage:')
    print('  ./manage.py clean - Clean build data')
    print('  ./manage.py package - create package from source')
    print('  ./manage.py publish - publish to PYPI')


def clean():
    os.system('rm -rf *.egg-info build dist')


def package():
    clean()
    os.system('./setup.py sdist bdist_wheel')


def publish():
    os.system('twine upload --repository pypi dist/*')


def main():
    if len(sys.argv) >= 2:
        cmd = sys.argv[1]
        actions = {
            'clean': clean,
            'package': package,
            'publish': publish,
        }
        if cmd in actions:
            return actions[cmd]()
    usage()


if __name__ == '__main__':
    main()
