from setuptools import setup

setup(
    name='distutils-licenses',
    version='0.1.0',
    description='adds a command to setup.py to list licenses of packages',
    author='Daniel A. Koepke',
    author_email='dkoepke@gmail.com',
    license="MIT",

    entry_points={
        'distutils.commands': [
            'licenses = licenses:LicenseCommand',
        ],
    }
)
