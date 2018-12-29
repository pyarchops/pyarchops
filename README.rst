=====================
pyArchOps
=====================


.. image:: https://badge.fury.io/py/pyarchops-pyarchops.svg
        :target: https://pypi.python.org/pypi/pyarchops

.. image:: https://img.shields.io/gitlab/pipeline/pyarchops/pyarchops/next-release.svg
        :target: https://gitlab.com/pyarchops/pyarchops/pipelines

.. image:: https://readthedocs.org/projects/pyarchops/badge/?version=latest
        :target: https://pyarchops.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/pyarchops/pyarchops/shield.svg
     :target: https://pyup.io/repos/github/pyarchops/pyarchops/
          :alt: Updates


pyarchops


* Free software: MIT license
* Documentation: https://pyarchops.readthedocs.io.


Features
--------

* pyarchops

Instalation
--------------

.. code-block:: console

    $ pip install pyarchops


Usage
--------

.. code-block:: python

    import os
    import pyarchops
    from suitable import Api

    api = Api(
        '127.0.0.1:22',
        connection='smart',
        remote_user='root',
        private_key_file=os.getenv('HOME') + '/.ssh/id_rsa',
        become=True,
        become_user='root',
        sudo=True,
        ssh_extra_args='-o StrictHostKeyChecking=no'
    )
    result = pyarchops.os_updates.apply(api)
    print(result)


See the different README pages for the different modules:

* https://github.com/pyarchops/dnsmasq
* https://github.com/pyarchops/helpers
* https://github.com/pyarchops/os-updates
* https://github.com/pyarchops/tinc


Development
-----------

Install requirements:

.. code-block:: console

    $ sudo pacman -S tmux python-virtualenv python-pip libjpeg-turbo gcc make vim git tk tcl

Git clone this repository

.. code-block:: console

    $ git clone https://github.com/pyarchops/pyarchops.git pyarchops.pyarchops
    $ cd pyarchops.pyarchops


2. See the `Makefile`, to get started simply execute:

.. code-block:: console

    $ make up


Credits
-------

* TODO

