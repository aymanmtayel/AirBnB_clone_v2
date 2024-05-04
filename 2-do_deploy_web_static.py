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
    if (ar_path is None):
        return False
    try:
        file_p = ar_path.split("/")[-1]
        file = file_p.split(".")[0]
        server_path = "/tmp/{}".fomat(file_p)
        versions_path = "/data/web_static/releases/{}/".format(file)
        put(ar_path, server_path)
        run("mkdir -p {}".format(versions_path))
        run("tar -xzf {} -C {}".format(server_path, versions_path))
        run("rm {}".format(server_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(versions_path))
        return True
    except Exception:
        return False
