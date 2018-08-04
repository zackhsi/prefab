from setuptools import setup


setup(
    name='prefab',
    version='0.1.0',
    description='Prefabricate a python project!',
    url='http://github.com/zackhsi/prefab',
    author='Zack Hsi',
    author_email='zackhsi@gmail.com',
    license='MIT',
    packages=['prefab'],
    entry_points={
        'console_scripts': [
            'prefab = prefab.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
