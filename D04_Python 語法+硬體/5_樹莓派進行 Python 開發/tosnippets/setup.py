from setuptools import setup

setup(
    name='tosnippets',
    version='0.1',
    scripts=['tosnippets.py'],
    entry_points={
        'console_scripts': [
            'tosnippets = tosnippets:main',
        ],
    },
)
