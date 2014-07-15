from fabric.api import *
from fabtools import require
import fabtools
import yaml


# Fabfile settings
settings_file = 'settings.yaml'

hosts_list = ['192.168.1.107:8200']
env.hosts = ['thiago@192.168.1.107:8200']
env.passwords = {
    'thiago@192.168.1.107:8200': 'thi2003'
}
env.roledefs = {
    'web': [hosts_list[0]],
    'mail': [hosts_list[0]]
}


def load_settings(settings=settings_file):
    '''
    Load settings.yaml
    This file contain:
        - variables for templates
        - packages for installation
        - sources and destination folders
        - etc
    '''
    try:
        with open(settings) as stream:
            data = yaml.load(stream)
            return data
    except IOError as error:
        print ('File error: ' + str(error))


@task
def server_shutdown(time='now'):
    '''
    Shutdown server in a time (default=now)
    '''
    run('sudo shutdown -h ' + time)


@task
def server_restart():
    '''
    Restart server
    '''
    run('sudo restart -n')


@task
def repository_update():
    '''
    Update APT package definitions (apt-get update).
    Only if specified time since last update already elapsed.
    '''
    require.deb.uptodate_index(max_age={'day': 1})


@task
def packages_install():
    '''
    Require several deb packages to be installed.
    Set packages to be installed at settings.yaml.
    '''
    load_settings()
    repository_upgrade()
    require.deb.packages(data['packages'])


@task
def service_restart(service=None):
    '''
    Require a service to be restarted.
    '''
    require.service.restarted(service)


@task
def service_start(service=None):
    '''
    Require a service to be started.
    '''
    require.service.started(service)


@task
def service_stop(service=None):
    '''
    Require a service to be stopped.
    '''
    require.service.stopped(service)


@task
def service_running(service=None):
    '''
    Check if service is running.
    '''
    if fabtools.service.is_running(service):
        print "Service is running!"


@task
def upload_templates(template=None):
    '''
    Generate config files from templates and upload to server.
    Default template is none. Define templates in settings.yaml.
    '''
    load_settings()
    fabtools.files.upload_template(data[template]['template'],
                                   data[template]['destination'],
                                   context=data[template]['settings'],
                                   use_jinja=True,
                                   template_dir=data[template]['source'],
                                   use_sudo=True, backup=True,
                                   mirror_local_mode=False, mode=None,
                                   mkdir=False, chown=False,
                                   user=None
                                   )
