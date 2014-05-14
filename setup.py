from setuptools import setup

setup(
    name='distutils-licenses',
    version='0.1.0',

    author='Daniel A. Koepke',
    author_email='dkoepke@gmail.com',
    license='MIT',

    description='adds a command to setup.py to list licenses of packages',
    long_description=open('README.md').read(),

    url='http://github.com/dkoepke/distutils-licenses',

    entry_points={
        'distutils.commands': [
            'licenses = licenses:LicenseCommand',
        ],
    }
)
