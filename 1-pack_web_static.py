#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""

from datetime import datetime
from fabric.api import local
from fabric.decorators import task

@task
def do_pack():
    """task to create a .tgz archive from the contents
    of the web_static folder
    """
    local("mkdir -p versions")
    t = datetime.now()
    name = "web_static_{}{}{}{}{}{}.tgz".format(
            t.year, t.month, t.day, t.hour, t.minute, t.second)
    file = local("tar -cvzf versions/{} web_static".format(name))
    if file.succeeded:
        return "versions/{}".format(name)
    else:
        return None
