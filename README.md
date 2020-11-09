# pyOGCAPI
An Async-First, modern OGC-API server for Python 3.6+

[![Build Status](https://travis-ci.org/ashleysommer/pyogcapi.svg?branch=master)](https://travis-ci.org/ashleysommer/pyogcapi) [![Coverage Status](https://coveralls.io/repos/github/ashleysommer/pyogcapi/badge.svg?branch=master)](https://coveralls.io/github/ashleysommer/pyogcapi?branch=master) [![PyPI version](https://badge.fury.io/py/pyogcapi.svg)](https://badge.fury.io/py/pyogcapi) [![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Downloads](https://pepy.tech/badge/pyogcapi)](https://pepy.tech/project/pyogcapi) [![Downloads](https://pepy.tech/badge/pyogcapi/month)](https://pepy.tech/project/pyogcapi/month) [![Downloads](https://pepy.tech/badge/pyogcapi/week)](https://pepy.tech/project/pyogcapi/week)

This python module is an OGC-API server implementation, similar to that provided by [PyGeoAPI](https://pygeoapi.io/).

Differences between PyGeoAPI and pyOGCAPI include:
- Async First
  - pyOGCAPI uses async providers and an async HTTP server, for fast and efficient execution.
  - pyOGCAPI uses the Sanic HTTP server, which is async and ASGI-compatibile
  - This library can be deployed natively using [uvicorn](http://www.uvicorn.org/).
- License
  - While both projects are Open-Source, pyOGCAPI is provided under the "Apache-2.0" license.
  - PyGeoAPI uses the MIT Open Source license.
- Use as a python module
  - PyGeoAPI is a standalone application, whereas pyOGCAPI can be imported as a server library into your existing application
- Powerful, Extensible Plugin System
  - PyOGCAPI uses the pyutil.components.core Component Plugin implementation, inspired by the Plugins subsystem of CKAN.
- No Shared Code
  - pyOGCAPI is a completely independent OGC-API implementation, it does not share or borrow any source code from PyGeoAPI or any other OGC-API implementation.
- PEP-517/PEP-519
  - pyOGCAPI is a PEP-517 based python project, it uses Poetry to manage its dependencies and create release builds

Similarities between PyGeoAPI and pyOGCAPI include:
- Configuration
  - pyOGCAPI uses the same Configuration file YAML format.
  - PyGeoAPI configuration files should work fine in pyOGCAPI.
- Routes
  - Given both pyOGCAPI and PyGeoAPI both implement the OGC-API specifications, they share a lot of web routing logic
- Providers
  - pyOGCAPI has built in many of the same backend data provider types as PyGeoAPI
  - Provider Interface - Initially pyOGCAPI data provider modules implement the same module-level interface as PyGeoAPI, but that may change as pyOGCAPI evolves.
  - pyOGCAPI implements an _async_ version of each provider, eg using Motor for mongodb, aiofiles for filesystem, and asyncpg for postgresql
- Templates
  - pyOGCAPI uses HTML templates with a layout inspired by (but not copied from) HTML templates in PyGeoAPI.
  - There are only so many ways this kind of information can be presented, this way is familiar to most users.
- Logging
  - pyOGCAPI logging subsystem is configured in the same way as PyGeoAPI
  - pyOGCAPI emits many of the same or similar log messages as PyGeoAPI


## Installation
Install with PIP (Using the Python3 pip installer `pip3`)
```bash
$ pip3 install pyogcapi
```

Or in a python virtualenv _(these example commandline instructions are for a Linux/Unix based OS)_
```bash
$ python3 -m virtualenv --python=python3 .venv
$ source ./.venv/bin/activate
$ pip3 install pyogcapi
```

To exit the virtual enviornment:
```bash
$ deactivate
```


## Compatibility

pyOGCAPI is a Python3 library. For best compatibility use Python v3.6 or greater. Python3 v3.5 or below is _**not supported**_ and this library _**does not work**_ on Python v2.7.x or below.

pyOGCAPI is now a PEP518 & PEP517 project, it uses `pyproject.toml` and `poetry` to manage dependencies, build and install.

For best compatibility when installing from PyPI with `pip`, upgrade to pip v18.1.0 or above.
  - If you're on Ubuntu 16.04 or 18.04, you will need to run `sudo pip3 install --upgrade pip` to get the newer version.

## Changelog

A comprehensive changelog is kept in the [CHANGELOG file](https://github.com/ashleysommer/pyogcapi/blob/master/CHANGELOG.md).


## License

This repository is licensed under Apache License, Version 2.0. See the [LICENSE deed](https://github.com/ashleysommer/pyogcapi/blob/master/LICENSE.txt) for details.


## Contributors

See the [CONTRIBUTORS file](https://github.com/ashleysommer/pyogcapi/blob/master/CONTRIBUTORS.md).


## Contacts

Lead Developer:  
**Ashley Sommer**  
*Informatics Software Engineer*  
CSIRO Land & Water, Environmental Informatics Group  
Brisbane, Qld, Australia  
<Ashley.Sommer@csiro.au>  
<https://orcid.org/0000-0003-0590-0131>  
