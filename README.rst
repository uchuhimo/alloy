
alo
===


.. image:: https://img.shields.io/pypi/v/alo.svg
   :target: https://pypi.python.org/pypi/alo
   :alt: 


.. image:: https://img.shields.io/travis/uchuhimo/alo.svg
   :target: https://travis-ci.org/uchuhimo/alo
   :alt: 


.. image:: https://github.com/uchuhimo/alo/workflows/Python%20package/badge.svg
   :target: https://github.com/uchuhimo/alo/actions
   :alt: 


.. image:: https://readthedocs.org/projects/alo/badge/?version=latest
   :target: https://alo.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status


.. image:: https://pyup.io/repos/github/uchuhimo/alo/shield.svg
   :target: https://pyup.io/repos/github/uchuhimo/alo/
   :alt: Updates


A tool to combine function with DAG.


* Documentation: https://alo.readthedocs.io.

Development
-----------

Create a virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   conda env create -f environment.yml
   source activate alo

Install dependencies
^^^^^^^^^^^^^^^^^^^^

There are two options:


* 
  Use poetry:

  .. code-block:: bash

       poetry install

* 
  Use pip:

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

Show information about installed packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   poetry show

Show dependency tree
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   dephell deps tree
   # or
   dephell deps tree pytest

Install git pre-commit hooks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   pre-commit install

License
=======

© uchuhimo, 2019. Licensed under an `Apache 2.0 <./LICENSE>`_ license.
