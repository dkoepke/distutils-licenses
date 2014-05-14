distutils-licenses
==================

A command for setup.py to print the licenses of installed packages.

To use, add `distutils-licenses` to the `setup_requires` keyword arg to the `setup` call in your `setup.py`:

```python
setup(
    # ...
    setup_requires=['distutils-licenses'],
    # ...
)
```

After modifying your `setup.py`, you will have a `licenses` command available to you:

```bash
python setup.py licenses
```

