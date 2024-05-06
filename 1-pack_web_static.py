#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """task to create a .tgz archive from the contents
    of the web_static folder
    """
    try:
        local("mkdir -p versions")
        TA = datetime.now()
        name = "web_static_{}{}{}{}{}{}.tgz".format(
                TA.year, TA.month, TA.day, TA.hour, TA.minute, TA.second)
        file = local("tar -cvzf versions/{} web_static".format(name))
        return "versions/{}".format(name)
    except Exception:
        return None
