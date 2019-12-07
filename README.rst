
Alloy
=====


.. image:: https://img.shields.io/pypi/v/alloy.svg
   :target: https://pypi.python.org/pypi/alloy
   :alt: 


.. image:: https://img.shields.io/travis/uchuhimo/alloy.svg
   :target: https://travis-ci.org/uchuhimo/alloy
   :alt: 


.. image:: https://github.com/uchuhimo/alloy/workflows/Python%20package/badge.svg
   :target: https://github.com/uchuhimo/alloy/actions
   :alt: 


.. image:: https://readthedocs.org/projects/alloy/badge/?version=latest
   :target: https://alloy.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


.. image:: https://pyup.io/repos/github/uchuhimo/alloy/shield.svg
   :target: https://pyup.io/repos/github/uchuhimo/alloy/
   :alt: Updates


A tool to combine function with DAG.


* Documentation: https://alloy.readthedocs.io.

Development
-----------

Create a virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   conda env create -f environment.yml
   source activate alloy

Install dependencies
^^^^^^^^^^^^^^^^^^^^

There are two options:


* Use poetry:
  .. code-block:: bash

       poetry install

* Use pip:
  .. code-block:: bash

       pip install -e ".[dev]"

Update dependencies
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   poetry update

Bump version
^^^^^^^^^^^^

.. code-block:: bash

   bumpversion minor  # major, minor, patch

Shows information about installed packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   poetry show

Install git pre-commit hooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   pre-commit install

License
=======

© uchuhimo, 2019. Licensed under an `Apache 2.0 <./LICENSE>`_ license.
