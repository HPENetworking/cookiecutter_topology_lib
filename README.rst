=========================
cookiecutter_topology_lib
=========================

About
=====

HPE Python project repository template for Topology Communication Libraries.

This cookiecutter is based on:

https://github.com/HPENetworking/cookiecutter_python

See also https://github.com/audreyr/cookiecutter.

- Open Source license: Apache 2.0.
- Automation setup using Tox_ for Python 2.7 and Python 3.4.
- Testing setup with pytest_.

  - Generates execution and coverage XML reports.
  - Autodiscovery and execution of doctest_.

- PEP8 compliance checking with Flake8_.

  - Includes a git pre-commit hook.
  - Includes configuration using EditorConfig_.

- Documentation setup with Sphinx_.

  - Automatic API generation using AutoAPI_.
  - Built-in support for PlantUML_ diagrams.

- Lightweight Python source distribution for PyPI.


Usage
=====

Generate a new Topology Communication Library using this template:

::

   pip install cookiecutter
   cookiecutter git@github.com:HPENetworking/cookiecutter_topology_lib.git

Once that is ready, add your library functions to
``lib/topology_lib_{{cookiecutter.library_name}}/library.py``.

.. _Tox: https://testrun.org/tox/
.. _pytest: http://pytest.org/
.. _doctest: https://docs.python.org/3/library/doctest.html
.. _Flake8: https://flake8.readthedocs.org/
.. _EditorConfig: http://editorconfig.org/
.. _Sphinx: http://sphinx-doc.org/
.. _AutoAPI: http://autoapi.readthedocs.org/
.. _PlantUML: http://plantuml.com/
