from fabric.api import *
import fabric.contrib.project as project
import os
import os.path
import sys
import SimpleHTTPServer
import SocketServer

# Setup for NAT busting/EC2
env.forward_agent = True
env.disable_known_hosts = True
env.gateway = 'teamunpro.com'
ssh_root = os.path.expanduser("~") + "/.ssh"
keys = ["teamunpro.pem", "id_rsa"]
env.key_filename = [ssh_root + "/" + k for k in keys]

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'pelican@10.0.1.12:22'
dest_path = '/srv/http/blog.teamunpro.com/html'

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    os.chdir(env.deploy_path)

    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        ssh_opts="-A ec2-user@teamunpro.com ssh",
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )
