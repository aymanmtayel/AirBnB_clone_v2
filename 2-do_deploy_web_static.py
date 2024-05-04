#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import put, run, env
from os.path import exists

env.user = 'ubuntu'
env.key_filename = '~/ALX/id_rsa'
env.hosts = ['54.237.41.246', '18.207.1.177']


def do_deploy(ar_path):
    """
    deploy our configs to our servers
    """
    if exists(ar_path) is False:
        return False
    try:
        file_p = ar_path.split("/")[-1]
        file = file_p.split(".")[0]
        server_path = "/tmp/"
        versions_path = "/data/web_static/releases/"
        put(ar_path, server_path)
        run("mkdir -p {}{}".format(versions_path, file))
        run("tar -xzf {} -C {}{}".format(server_path, file_p, versions_path, file))
        run("rm {}{}".format(server_path, file_p))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(versions_path, file))
        return True
    except:
        return False
