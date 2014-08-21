from fabric.api import *
import fabtools
import fabtools.require


@task
def restart(service=None):
    '''
    Require a service to be restarted.
    '''
    require.service.restarted(service)


@task
def start(service=None):
    '''
    Require a service to be started.
    '''
    require.service.started(service)


@task
def stop(service=None):
    '''
    Require a service to be stopped.
    '''
    require.service.stopped(service)


@task
def running(service=None):
    '''
    Check if service is running.
    '''
    if fabtools.service.is_running(service):
        print "Service is running!"
