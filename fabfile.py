from fabric.api import *
import fabtools
from tasks import (deb,
                   server,
                   service)

# Fabfile settings
"""
settings_file = ''

hosts_list = ['192.168.1.107:8200']
env.hosts = ['thiago@192.168.1.107:8200']
env.passwords = {
    'thiago@192.168.1.107:8200': 'thi2003'
}
env.roledefs = {
    'web': [hosts_list[0]],
    'mail': [hosts_list[0]]
}
"""

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
                                   use_sudo=True,
                                   backup=True,
                                   mirror_local_mode=False,
                                   mode=None,
                                   mkdir=False,
                                   chown=False,
                                   user=None
                                   )
