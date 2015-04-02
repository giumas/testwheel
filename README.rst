testwheel: testing wheel
==========================

.. image:: https://secure.travis-ci.org/giumas/testwheel.png
    :target: https://secure.travis-ci.org/giumas/testwheel


.. image:: https://coveralls.io/repos/giumas/testwheel/badge.svg
    :target: https://coveralls.io/r/giumas/testwheel


        
*testwheel* is an MIT_-licensed dummy Python module for testing wheel.


Utils
------

Use `bumpversion` to update the version for all files:

.. code-block:: python

    pip install --upgrade bumpversion
    pip install https://github.com/peritus/bumpversion/archive/master.zip#egg=bumpversion-dev


Build dist
----------

Distributions:

.. code-block:: python

    python setup.py sdist
    python setup.py bdist_wheel

Upload to PiPy
--------------

Create a HOME environ var with a folder where to store `.pypirc`:

.. code-block:: python

    [distutils]
    index-servers=
        pypi
        test
    
    [test]
    repository = https://testpypi.python.org/pypi
    username = <your test user name goes here>
    password = <your test password goes here>
    
    [pypi]
    repository = https://pypi.python.org/pypi
    username = <your production user name goes here>
    password = <your production password goes here>

    
Then:

.. code-block:: python

    python setup.py register -r pypi
    python setup.py register -r test
    python setup.py sdist upload -r pypi
    python setup.py sdist upload -r test
    python setup.py bdist_wheel upload -r pypi
    python setup.py bdist_wheel upload -r test


For testing if it works:

.. code-block:: python

    pip install testwheel
    pip install -i https://testpypi.python.org/pypi testwheel   


Testing
---------

.. code-block:: python

    pip install -U pytest
    py.test --version
    
    pip install tox
    tox
    
Future
------

I don't know!

.. _MIT: http://choosealicense.com/licenses/mit/