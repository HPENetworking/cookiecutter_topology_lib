# -*- coding: utf-8 -*-
#
# Copyright (C) {{ cookiecutter.year }} {{ cookiecutter.author }}
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
topology_lib_{{ cookiecutter.library_name }} communication library implementation.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

# Add your library functions here.


def your_function_here(enode, your_param, shell=None):
    """
    Document your function here.

    :param topology.platforms.base.BaseNode enode: Engine node to communicate
     with.
    :param bool your_param: This is an example parameter, read the comment
     below.
    :param str shell: Shell name to execute commands.
    """
    pass

    # Usually, the library functions use the parameters to build a command that
    # is to be sent to the enode, for example:
    #
    # command = 'echo "something"'
    # if your_param:
    #     command = '{command} "and something else"'.format(command=command)
    #
    # Then, the enode is used to send the command:
    #
    # enode('the command to be sent', shell=shell)

__all__ = [
    # The Topology framework loads the functions that are in this list to be
    # used as libraries, so, if you want your function to be loaded, add it
    # here.
    'your_function_here'
]
