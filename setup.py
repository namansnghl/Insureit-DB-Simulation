from setuptools import setup, find_packages

setup(
    name='insurit',
    version='0.1.0',
    packages=find_packages(),
    package_dir={'backend': 'insurit/backend'},
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'insurit = insurit.__main__:main',
        ]
    },
    license='MIT',
    author=', '.join(['Naman Singhal', 'Karan Badlani', 'Isha Singh']),
    url="https://github.com/namansnghl/Insureit-DB-Simulation"
)
