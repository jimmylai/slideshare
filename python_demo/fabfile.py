#!/usr/bin/env python
# -*- encoding: utf8 -*-
'''Program
'''

from fabric.api import local, prefix, sudo, hosts, run


__author__ = 'noahsark'


def search(word=None):
    if word is None:
        print 'Please specify `word` to search as argument.'
    else:
        local('find | xargs -i grep -H --color %s {}' % word)


def doc():
    with prefix('cd doc'):
        local('make html')


def test():
    local('nosetests --with-doctest --with-xunit --traverse-namespace --with-coverage '
          '--cover-package=python_demo')


def clean():
    '''remove pyc files.'''
    local('find | grep \.pyc$ | xargs -i rm -f {}')


def ci():
    test()
    doc()
    local('clonedigger --ignore-dir=classifier .')


@hosts('localhost')
def setup():
    # packages with system package support
    packages = ['numpy', 'scipy', 'matplotlib', 'pandas', 'coverage', 'nose',
                'sphinx', 'nltk', 'nose', 'xlwt', 'xlrd', 'jinja2', 'psutil']

    sudo('apt-get install -y python-virtualenv')
    sudo('apt-get install -y python-pip')
    run('virtualenv --no-site-packages env')

    for package in packages:
        sudo('apt-get build-dep -y python-%s' % package)
        with prefix('. env/bin/activate'):
            run('pip install %s' % package)

    # packages has no system packages
    packages = ['ipython', 'scikit-learn', 'pep8']
    for package in packages:
        with prefix('. env/bin/activate'):
            run('pip install %s' % package)
