# -*- coding: utf-8 -*-
# python

import subprocess

command = "python"
file_to_execute = ["setup.py", "configure.py"]
subprocess.check_call([command, file_to_execute[0], "install"])
subprocess.check_call([command, file_to_execute[1]])