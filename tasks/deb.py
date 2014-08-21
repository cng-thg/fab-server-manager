from __future__ import print_function
from fabric.api import *
from fabtools import require
import fabtools
from utils.settings import load_settings


settings_file = 'packages.yaml'


@task
def update():
    '''
    Update APT package definitions (apt-get update).
    Only if specified time since last update already elapsed.
    '''
    require.deb.uptodate_index(max_age={'day': 1})


@task
def pkg(packages=load_settings(settings_file)):
    '''
    Require deb packages to be installed (string or list).
    Set packages to be installed at settings.yaml.
    '''
    data = packages

    if type(data) == str:
        print(data)
    if type(data) == dict:
        if type(data['packages']) == list:
            print(data['packages'])


@task
def install(packages):
    '''
    Require deb packages to be installed (string or list).
    Set packages to be installed at settings.yaml.
    '''
    data = packages

    update()

    if type(data) == str:
        require.deb.package(data)
    if type(data) == dict:
        if type(data['packages']) == list:
            require.deb.packages(data['packages'])


@task
def remove(packages):
    '''
    Require deb packages to be removed (string or list).
    '''
    if type(data) == str:
        require.deb.nopackage(data)
    if type(data) == list:
        require.deb.nopackages(data)


@task
def upgrade(safe=True):
    '''
    Upgrade system packages (safe upgrade is default: safe=True)
    '''

    update()

    if safe:
        sudo('apt-get upgrade -y')
    else:
        sudo('apt-get dist-upgrade -y')
