from setuptools import setup

setup(
    name='insurit',
    version='0.1.0',
    packages=['insurit', 'backend'],
    entry_points={
        'console_scripts': [
            'insurit = insurit.__main__:main',
        ]
    })
