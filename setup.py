try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A System Environment manager.',
    'author': 'Harold Bradley III',
    'url': 'haroldbradleyiii.com',
    'download_url': 'haroldbradleyiii.com',
    'author_email': 'harold@bradleystudio.net',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'envi'
}

setup(**config)
