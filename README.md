distutils-licenses
==================

A command for setup.py to print the licenses of installed packages.

To use, place in your setup.py:

```python
setup_requires=['distutils-licenses']
```

Run:

```python
python setup.py develop
```

From then on, you can do:

```python
python setup.py licenses
```
