from setuptools import setup, find_packages

setup(
    name='arsy',
    version='0.1',
    py_modules=['arsy'],
    install_requires=[
        'Click',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'arsy = arsy:main'
        ]
    },
)
