from fabric.api import task, run


@task
def shutdown(time='now'):
    '''
    Shutdown server in a time (default=now)
    '''
    run('sudo shutdown -h ' + time)


@task
def reboot():
    '''
    Restart server
    '''
    run('sudo reboot -n')
