from setuptools import setup
setup(
    name = 'insureit',
    version = '0.1.0',
    packages = ['insurit'],
    entry_points = {
        'console_scripts': [
            'insurit = insurit.__main__:main'
        ]
    })
