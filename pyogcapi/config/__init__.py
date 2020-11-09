# -*- coding: utf-8 -*-
#
# Copyright 2020 Ashley Sommer <Ashley.Sommer@csiro.au>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING, Optional, Union, Dict, TextIO, Any
import re
import os
from os import path
import yaml
import mimetypes

mimetypes.add_type('text/plain', '.yaml')
mimetypes.add_type('text/plain', '.yml')


def str_to_python(value: str) -> Any:
    """
    Convert a node value (string) into python native equivalent
    :param value: incoming variable string
    :returns: value as a native Python data type
    :rtype: Any
    """

    try:
        if "." in value:
            # assume to be float
            ret = float(value)
        elif len(value) > 1 and value.startswith("0"):
            # Don't convert to int if it has a leading zero
            # We want to keep the zero, converting to int would remove it
            ret = value
        else:
            # try to convert to int
            ret = int(value)
    except ValueError:
        # conversion did not succeed, leave it as a string.
        ret = value
    return ret


def load_from_yaml_file(f: Union[str, TextIO]) -> Dict:
    """
    Parses a yaml file using PyYAML
    :param f: File handle or String
    :type f: Union[str, TextIO]
    :returns: config parsed from YAML file
    :rtype: Dict
    """

    # support environment variables in config
    # https://stackoverflow.com/a/55301129

    # For maximum compatibility with PyGeoApi config files, this function is
    # inspired by the yaml_load() function in pygeoapi/util.py here:
    # https://github.com/geopython/pygeoapi/blob/2c567d25f70daa3ed0a047ae548a3dfcd97c7cc2/pygeoapi/util.py#L100
    path_matcher = re.compile(r'.*\$\{([^}^{]+)\}.*')

    def path_constructor(loader, node):
        env_var = path_matcher.match(node.value).group(1)
        if env_var not in os.environ:
            raise EnvironmentError("Undefined environment variable in config")
        return str_to_python(path.expandvars(node.value))

    class EnvVarLoader(yaml.SafeLoader):
        pass

    EnvVarLoader.add_implicit_resolver('!path', path_matcher, None)
    EnvVarLoader.add_constructor('!path', path_constructor)
    do_close = False
    if isinstance(f, str):
        f = open(f, "r")
    resp = yaml.load(f, Loader=EnvVarLoader)
    if do_close:
        f.close()
    return resp


def load_server_config(config_file: Optional[str] = None) -> Dict:
    """
    :param config_file: filesystem location to find the yaml config file
    :type config_file: Optional[str]
    :return:
    """
    if config_file is None:
        try:
            config_file = os.environ['PYOGCAPI_CONFIG']
        except LookupError:
            try:
                config_file = os.environ['PYGEOAPI_CONFIG']
            except LookupError:
                pwd = os.getcwd()
                config_file = os.path.join(pwd, "pyogcapi-config.yaml")

    with open(config_file, "r") as f:
        config_dict = load_from_yaml_file(f)
    return config_dict

def get_config_part(config_parent, match_key, match_value):
    """
    helper function to filter a dict by a dict key

    :param dict_: ``dict``
    :param key: dict key
    :param value: dict key value

    :returns: filtered ``dict``
    """

    return {k: v for (k, v) in config_parent.items() if v[match_key] == match_value}
